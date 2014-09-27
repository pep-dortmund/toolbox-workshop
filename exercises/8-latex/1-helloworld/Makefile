all: build/1-helloworld.pdf


build/1-helloworld.pdf: 1-helloworld.tex | build
	lualatex --output-directory=build 1-helloworld
	lualatex --output-directory=build 1-helloworld

build:
	mkdir -p build

clean:
	rm -r build
