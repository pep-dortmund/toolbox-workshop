CONTENT := $(addprefix content/, $(addsuffix .tex, gleitumgebungen grundlagen matheumgebung siunitx standardpakete text))

build/latex.pdf: latex.tex $(CONTENT) | build
	@../common/tex.sh latex.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --fast latex.tex

clean:
	rm -rf build
