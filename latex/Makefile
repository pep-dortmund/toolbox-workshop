include ../common/common.mk

BIBER := --biber

include ../common/document.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os experience))

build/figures/tex-overview.pdf: | build/figures
	cp "$$(texdoc -l -M tex-overview.pdf | awk -F '\t' '{ print $$3 }')" $@

$(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$')))): build/figures/tex-overview.pdf

build/latex.pdf: $(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$'))))

build/figures/knuth.jpg: | build/figures
	wget https://www.cs.cmu.edu/sites/default/files/Knuth_b.jpg -O $@ --no-use-server-timestamps

build/figures/lamport.jpg: | build/figures
	wget http://amturing.acm.org/images/Lamport_2.jpg -O $@ --no-use-server-timestamps

build/latex.pdf: $(addprefix build/figures/, $(addsuffix .jpg, knuth lamport))

build/latex.pdf: examples.bib

build/latex.pdf: $(FIGURES)

MATTEX := $(addprefix build/figures/mattex, $(addsuffix .pdf, 1 2 3 4 5))

build/latex.pdf: $(MATTEX) $(addprefix script/mattex, $(addsuffix .py, 1 2 3 4 5)) matplotlibrc header-matplotlib.tex

$(FIGURES): script/answers.py data/2019.csv
	TEXINPUTS=$(shell pwd): python3 $<

build/figures/mattex%.pdf: script/mattex%.py matplotlibrc header-matplotlib.tex
	TEXINPUTS=$(shell pwd): python $<
