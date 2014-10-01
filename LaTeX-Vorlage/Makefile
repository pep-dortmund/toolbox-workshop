all: | build
	lualatex --output-directory=build main.tex
	biber --output-directory=build main.bcf
	lualatex --output-directory=build main.tex
	mv build/main.pdf main.pdf

build:
	mkdir -p build

clean:
	rm -rf build
