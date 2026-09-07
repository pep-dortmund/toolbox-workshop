include ../common/common.mk
include ../common/document.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os programming interest))
EXAMPLE_PLOT := build/example_plot.pdf
WGET_OPTIONS = --user-agent=ToolboxWorkshop/1.0 --no-use-server-timestamps

build/intro.pdf: $(FIGURES) $(EXAMPLE_PLOT) $(addprefix build/figures/, \
	real_programmers.png windows.png macos.png tux.jpg\
	)

build/figures/os.pdf: script/answers.py data/toolbox2025.json ../common/matplotlibrc ../common/header-matplotlib.tex
	sed -i "s/Habe den 'Grundlagen wissenschaftlicher Datenverarbeitung' Kurs besucht./Datenverarbeitungskurs,besucht./g" data/toolbox2025.json
	MATPLOTLIBRC=../common/matplotlibrc TEXINPUTS=$$(pwd)/../common: python3 $<

$(addprefix build/figures/, programming.pdf interest.pdf): build/figures/os.pdf

build/figures/real_programmers.png: | build/figures
	wget -O $@ ${WGET_OPTIONS} http://imgs.xkcd.com/comics/real_programmers.png

build/figures/windows.png: | build/figures
	wget -O $@  ${WGET_OPTIONS} https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Windows_logo_and_wordmark_-_2021.svg/1280px-Windows_logo_and_wordmark_-_2021.svg.png

build/figures/macos.png: | build/figures
	wget -O $@  ${WGET_OPTIONS} https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/MacOS_logo.svg/960px-MacOS_logo.svg.png

build/figures/tux.jpg: | build/figures
	wget ${WGET_OPTIONS} https://upload.wikimedia.org/wikipedia/commons/d/dd/Linux_logo.jpg -O build/figures/tux-original.jpg 
	magick build/figures/tux-original.jpg -trim $@

build/example_plot.pdf: script/example_plot.py | build/figures
	MATPLOTLIBRC=../common/matplotlibrc TEXINPUTS=$$(pwd)/../common: python3 $<
