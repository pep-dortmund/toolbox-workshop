#!/bin/bash

usage() {
	echo "Usage: $0 [--[no-]fast] [--jobname <jobname>] [--tex-inputs <tex-inputs>] [--[no-]biber] [--bib-inputs <bib-inputs>] <file.tex>"
	exit 1
}

warnings() {
	"$(dirname "$0")/log.py" "build/${JOBNAME}.log"
}

cleanup() {
	rm -f "build/${JOBNAME}.pdf"
	exit 2
}

tex_exec() {
	echo "\$TEX --jobname=\"${JOBNAME}\" \"${FILE}\""
	if ! eval $TEX_EXEC > /dev/null ; then
		warnings
		cleanup
	fi
}

biber_exec() {
	echo "\$BIBER \"build/${JOBNAME}.bcf\""
	eval ${BIBER_EXEC} | grep -E "^(WARN|ERROR)"
	if ! [ "${PIPESTATUS[0]}" -eq 0 ] ; then
		cleanup
	fi
}

fast() {
	tex_exec
	warnings
	exit 0
}

full() {
	tex_exec
	WARNINGS="$(warnings)"
	CODE="$?"

	if "${BIBER}" ; then
		if [ $((${CODE} & 4)) -eq 0 ] ; then
			RUN_BIBER=false
		else
			RUN_BIBER=true
		fi

		if [ -e "build/${JOBNAME}.bbl" ] ; then
			BBL_STAT="$(stat --format="%Y" "build/${JOBNAME}.bbl")"
		else
			BBL_STAT=0
		fi

		OLD_IFS="${IFS}"
		IFS=$'\n'
		BIB_FILES="$(xmllint --nocdata --xpath '/requests/external[@package="biblatex"][generic="biber"]/requires[@type="editable"]/file' "build/${JOBNAME}.run.xml" | sed 's/</\n</g' | sed 's/>/>\n/g' | grep -v '<\|>' | grep -v '^$')"
		for bib_file in ${BIB_FILES} ; do
			bib_file="$(find ${BIB_INPUTS//:/$'\n'} -maxdepth 1 -name "${bib_file}" -print -quit)"
			if [ -n "${bib_file}" ] && [ "${BBL_STAT}" -lt "$(stat --format="%Y" "${bib_file}")" ] ; then
				RUN_BIBER=true
			fi
		done
		IFS="${OLD_IFS}"

		if "${RUN_BIBER}" ; then
			biber_exec
		fi
	else
		RUN_BIBER=false
	fi

	if [ $((${CODE} & 2)) -eq 0 ] && ! "${RUN_BIBER}" ; then
		if [ -n "${WARNINGS}" ] ; then
			echo "${WARNINGS}"
		fi
		exit 0
	fi

	while true ; do
		tex_exec
		WARNINGS="$(warnings)"
		CODE="$?"
		if [ $((${CODE} & 2)) -eq 0 ] ; then
			if [ -n "${WARNINGS}" ] ; then
				echo "${WARNINGS}"
			fi
			exit 0
		fi
	done

	exit 0
}

if [ "$#" -eq 0 ] ; then
	usage
fi

if [ -n "${FAST}" ] && [ "${FAST}" != "0" ] ; then
	FAST=true
else
	FAST=false
fi

if [ -n "${BIBER}" ] && [ "${BIBER}" != "0" ] ; then
	BIBER=true
else
	BIBER=false
fi

while [ "$#" -gt 1 ] ; do
	case "$1" in
		"--fast")
			FAST=true
			;;
		"--no-fast")
			FAST=false
			;;
		"--jobname")
			if [ "$#" -eq 1 ] ; then
				usage
			fi
			JOBNAME="$2"
			shift
			;;
		"--tex-inputs")
			if [ "$#" -eq 1 ] ; then
				usage
			fi
			TEX_INPUTS="$2"
			shift
			;;
		"--biber")
			BIBER=true
			;;
		"--no-biber")
			BIBER=false
			;;
		"--bib-inputs")
			if [ "$#" -eq 1 ] ; then
				usage
			fi
			BIB_INPUTS="$2"
			shift
			;;
	esac
	shift
done

FILE="$1"

if [ -z "${JOBNAME}" ] ; then
	JOBNAME="${FILE%.tex}"
fi

if [ -n "${TEX_INPUTS}" ] ; then
	TEX_INPUTS=":${TEX_INPUTS}"
fi
TEX_INPUTS="$(pwd)/build/:$(pwd)/${TEX_INPUTS}:"

if [ -n "${BIB_INPUTS}" ] ; then
	BIB_INPUTS=":${BIB_INPUTS}"
fi
BIB_INPUTS="$(pwd)/build/:$(pwd)/${BIB_INPUTS}"

TEX_ENV="TEXINPUTS=\"${TEX_INPUTS}\" max_print_line=1048576"
TEX_ARG="--shell-escape --halt-on-error --interaction=batchmode --output-directory=build --jobname=\"${JOBNAME}\" \"${FILE}\""
TEX_EXEC="env ${TEX_ENV} lualatex ${TEX_ARG}"

BIBER_ENV="BIBINPUTS=\"${BIB_INPUTS}\""
BIBER_ARG="--logfile \"build/${JOBNAME}.blg\" --outfile \"build/${JOBNAME}.bbl\" \"build/${JOBNAME}.bcf\""
BIBER_EXEC="env ${BIBER_ENV} biber ${BIBER_ARG}"

if "${FAST}" ; then
	fast
else
	full
fi
