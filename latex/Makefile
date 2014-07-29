CONTENT := $(addprefix content/, $(addsuffix .tex, gleitumgebungen grundlagen matheumgebung siunitx standardpakete text))

build/slides.pdf: slides.tex $(CONTENT) | build
	@../common/tex.sh slides.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --fast slides.tex

clean:
	rm -rf build
