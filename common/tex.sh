#!/bin/bash

TEXENV="TEXINPUTS=\"$(pwd)/build/:$(pwd)/:$(pwd)/../common/:\" max_print_line=1048576"
TEXARG="--shell-escape --halt-on-error --interaction=batchmode --output-directory=build"
TEX="env $TEXENV lualatex $TEXARG"

BIBERENV="BIBINPUTS=\"$(pwd)/build/:$(pwd)/:$(pwd)/../common/\""
BIBER="env $BIBERENV biber"

usage() {
	echo "Usage: $0 [--fast|--full] file [jobname]"
	exit 1
}

fast() {
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		warnings "$2"
		rm -f build/"$2".pdf
		exit 1
	else
		warnings "$2"
	fi
}

full() {
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		warnings "$2"
		rm -f build/"$2".pdf
		exit 1
	fi
	echo '$BIBER' --logfile build/"$2".blg --outfile build/"$2".bbl build/"$2".bcf
	eval $BIBER --logfile build/"$2".blg --outfile build/"$2".bbl build/"$2".bcf | grep -E "^(WARN|ERROR)"
	if ! [ ${PIPESTATUS[0]} -eq 0 ] ; then
		rm -f build/"$2".pdf
		exit 1
	fi
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		warnings "$2"
		rm -f build/"$2".pdf
		exit 1
	fi
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		warnings "$2"
		rm -f build/"$2".pdf
		exit 1
	else
		warnings "$2"
	fi
}

warnings() {
	pushd build >/dev/null
	if hash rubber-info 2>/dev/null ; then
		rubber-info --errors "$1".log
		rubber-info --warnings "$1".log
		rubber-info --refs "$1".log
		rubber-info --boxes "$1".log
	else
		tail -n 30 "$1".log
	fi
	popd >/dev/null
}

case $# in
	0 )
		usage
		;;
	1 )
		"$0" "$1" "${1%.*}"
		;;
	2 )
		case "$1" in
			"--fast" | "--full" )
				"$0" "$1" "$2" "${2%.*}"
				;;
			* )
				"$0" --full "$1" "$2"
				;;
		esac
		;;
	3 )
		case "$1" in
			"--fast" )
				METHOD=fast
				;;
			"--full" )
				METHOD=full
				;;
			* )
				usage
				;;
		esac
		if [[ ! -z "$TEX_FAST" ]] ; then
			if [ "$TEX_FAST" -ne 0 ] ; then
				METHOD=fast
			else
				METHOD=full
			fi
		fi
		$METHOD "$2" "$3"
		;;
esac
