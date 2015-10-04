include ../common/common.mk

all: $(patsubst %.ipynb, %.html, $(wildcard *.ipynb))

%.html: %.ipynb
	jupyter-nbconvert --execute --allow-errors --to html $<

muon_plot.png: muon_plot.py muon_data.txt
	python3 $<

clean:
	git clean -Xdf

.PHONY: all clean
