include ../common/common.mk
include ../common/document.mk


MATPLOTLIBRC :=  ../common/matplotlibrc
MPLHEADER := ../common/header-matplotlib.tex

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os experience))

build/figures/tex-overview.pdf: | build/figures
	cp "$$(texdoc -l -M tex-overview.pdf | awk -F '\t' '{ print $$3 }')" $@

$(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$')))): build/figures/tex-overview.pdf

build/latex.pdf: $(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$'))))

build/latex.pdf: examples.bib

build/latex.pdf: $(FIGURES)

MATTEX := $(addprefix build/figures/mattex, $(addsuffix .pdf, 1 2 3 4 5))

build/latex.pdf: $(MATTEX)

$(FIGURES): script/answers.py ../intro/data/toolbox2023.json ${MATPLOTLIBRC} ${MPLHEADER}
	TEXINPUTS=$$(pwd)/../common: MATPLOTLIBRC=${MATPLOTLIBRC} python $<

build/figures/mattex%.pdf: script/mattex%.py
	TEXINPUTS=$$(pwd)/../common: python $<

build/figures/mattex5.pdf: script/mattex5.py ${MATPLOTLIBRC} ${MPLHEADER}
	TEXINPUTS=$$(pwd)/../common: MATPLOTLIBRC=${MATPLOTLIBRC} python $<
