include ../common/common.mk

all: $(addprefix build/, $(patsubst %.ipynb, %.html, $(wildcard *.ipynb)))


# build/python.html: build/muon_plot.png

build/%.html: %.ipynb
	jupyter-nbconvert --output-dir=build --execute --allow-errors --to html --template classic $<

build/muon_plot.png: muon_plot.py data/muon_data.txt
	TEXINPUTS=$$(pwd): MATPLOTLIBRC=matplotlibrc_muon python3 $<

clean:
	git clean -Xdf

.PHONY: all clean
