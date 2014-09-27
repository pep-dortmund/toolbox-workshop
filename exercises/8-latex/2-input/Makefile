all: build/loesung.pdf


build/loesung.pdf: loesung.tex helloworld.tex header.tex | build
	lualatex --output-directory=build loesung
	lualatex --output-directory=build loesung

build:
	mkdir -p build

clean:
	rm -r build
