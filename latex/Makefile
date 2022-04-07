include ../common/common.mk

BIBER := --biber

include ../common/document.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os experience))

build/figures/tex-overview.pdf: | build/figures
	cp "$$(texdoc -l -M tex-overview.pdf | awk -F '\t' '{ print $$3 }')" $@

$(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$')))): build/figures/tex-overview.pdf

build/latex.pdf: $(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$'))))

build/latex.pdf: examples.bib

build/latex.pdf: $(FIGURES)

MATTEX := $(addprefix build/figures/mattex, $(addsuffix .pdf, 1 2 3 4 5))

build/latex.pdf: $(MATTEX) $(addprefix script/mattex, $(addsuffix .py, 1 2 3 4 5)) script/matplotlibrc header-matplotlib.tex

$(FIGURES): script/answers.py ../intro/data/toolbox2021.json
	TEXINPUTS=$$(pwd): python $<

build/figures/mattex%.pdf: script/mattex%.py script/matplotlibrc header-matplotlib.tex
	TEXINPUTS=$$(pwd): python $<

build/figures/mattex5.pdf: script/mattex5.py script/matplotlibrc header-matplotlib.tex
	TEXINPUTS=$$(pwd): MATPLOTLIBRC=script/matplotlibrc python $<
