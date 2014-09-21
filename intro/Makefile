include ../common/common.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os programming interest))

build/intro.pdf: $(FIGURES)

$(FIGURES): script/answers.py data/answers.tsv
	python3 $<
