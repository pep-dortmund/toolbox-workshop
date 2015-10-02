texoptions = -lualatex \
			 -interaction=nonstopmode \
			 -output-directory=build \
			 -halt-on-error

texinputs = .:../common:

all: #build/teaser.pdf

build/teaser.pdf: teaser.tex | build
	TEXINPUTS=$(texinputs) texfot latexmk $(texoptions) teaser.tex

build:
	mkdir -p build

clean:
	rm -rf build
