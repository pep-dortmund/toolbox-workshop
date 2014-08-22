CONTENT := $(addprefix content/, $(addsuffix .tex, aufzaehlungen gleitumgebungen grundlagen matheumgebung siunitx standardpakete text))

build/latex.pdf: latex.tex $(CONTENT) | build
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" latex.tex

build:
	mkdir -p build

fast:
	@../common/tex.sh --tex-inputs "$(shell pwd)/../common/" --fast latex.tex

clean:
	rm -rf build
