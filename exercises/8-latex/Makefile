all: build/exercise-template.pdf


build/exercise-template.pdf: exercise-header.tex exercise-template.tex | build
	lualatex --output-directory=build exercise-template
	lualatex --output-directory=build exercise-template

build:
	mkdir -p build

clean:
	rm -r build
