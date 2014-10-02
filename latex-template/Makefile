all: main.pdf
	
main.pdf: content/*.tex header.tex lit.bib main.tex | build
	max_print_line=1048576 TEXINPUTS=build:.: lualatex --output-directory=build --interaction=nonstopmode --halt-on-error main.tex
	BIBINPUTS=build:. biber build/main.bcf
	max_print_line=1048576 TEXINPUTS=build:.: lualatex --output-directory=build --interaction=nonstopmode --halt-on-error main.tex
	max_print_line=1048576 TEXINPUTS=build:.: lualatex --output-directory=build --interaction=nonstopmode --halt-on-error main.tex

build:
	mkdir -p build

clean:
	rm -rf build
