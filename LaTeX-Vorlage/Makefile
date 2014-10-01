all: main.pdf
	
main.pdf: content/*.tex res/header.tex res/lit.bib main.tex| build
	lualatex --output-directory=build main.tex
	biber build/main.bcf
	lualatex --output-directory=build main.tex
	mv build/main.pdf main.pdf

build:
	mkdir -p build

clean:
	rm -rf build
