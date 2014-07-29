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
	    cd build
	    rubber-info --errors "$2".log
	    rubber-info --warnings "$2".log
	    rubber-info --refs "$2".log
	    rubber-info --boxes "$2".log
	    rm -f "$2".pdf
	    exit 1
	else
	    cd build
	    rubber-info --errors "$2".log
	    rubber-info --warnings "$2".log
	    rubber-info --refs "$2".log
	    rubber-info --boxes "$2".log
	fi
}

full() {
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		cd build
		rubber-info --errors "$2".log
		rubber-info --warnings "$2".log
		rubber-info --refs "$2".log
		rubber-info --boxes "$2".log
		rm -f "$2".pdf
		exit 1
	fi
	echo '$BIBER' --logfile build/"$2".blg --outfile build/"$2".bbl build/"$2".bcf
	eval $BIBER --logfile build/"$2".blg --outfile build/"$2".bbl build/"$2".bcf | grep -E "^(WARN|ERROR)"
	if ! [ ${PIPESTATUS[0]} -eq 0 ] ; then
		rm -f "$2".pdf
		exit 1
	fi
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		cd build
		rubber-info --errors "$2".log
		rubber-info --warnings "$2".log
		rubber-info --refs "$2".log
		rubber-info --boxes "$2".log
		rm -f "$2".pdf
		exit 1
	fi
	echo '$TEX' --jobname="$2" "$1"
	if ! eval $TEX --jobname="$2" "$1" > /dev/null ; then
		cd build
		rubber-info --errors "$2".log
		rubber-info --warnings "$2".log
		rubber-info --refs "$2".log
		rubber-info --boxes "$2".log
		rm -f "$2".pdf
		exit 1
	else
		cd build
		rubber-info --errors "$2".log
		rubber-info --warnings "$2".log
		rubber-info --refs "$2".log
		rubber-info --boxes "$2".log
	fi
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
