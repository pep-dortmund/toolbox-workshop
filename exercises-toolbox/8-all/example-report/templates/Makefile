all: build/v16516.pdf

# hier Python-Skripte:
build/plot-I_kugel.pdf build/plot-I_zylinder.pdf build/plot-g_kugel.pdf build/plot-g_zylinder.pdf: auswertung.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python auswertung.py

# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/v16516.pdf: build/plot-I_kugel.pdf build/plot-I_zylinder.pdf build/plot-g_kugel.pdf build/plot-g_zylinder.pdf

build/v16516.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v16516.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
