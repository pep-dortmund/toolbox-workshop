all: build/v16516.pdf

# hier Python-Skripte:
build/plot-g_ball.pdf: auswertung.py ../matplotlibrc ../header-matplotlib.tex data/*| build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python auswertung.py

build/parameter-g_ball.tex: build/plot-g_ball.pdf
build/parameter-t0-g_ball.tex: build/parameter-g_ball.tex

build/plot-g_cylinder.pdf: build/parameter-t0-g_ball.tex
build/parameter-g_cylinder.tex: build/plot-g_cylinder.pdf
build/parameter-t0-g_cylinder.tex: build/parameter-g_cylinder.tex

build/plot-I_ball.pdf: build/parameter-g_cylinder.tex
build/parameter-I_ball.tex: build/plot-I_ball.pdf
build/parameter-t0-I_ball.tex: build/parameter-I_ball.tex

build/plot-I_cylinder.pdf: build/parameter-t0-I_ball.tex
build/parameter-I_cylinder.tex: build/plot-I_cylinder.pdf
build/parameter-t0-I_cylinder.tex: build/parameter-I_cylinder.tex

build/table_all-measurements.tex: build/parameter-t0-I_cylinder.tex
build/table_averaged-measurements.tex: build/table_all-measurements.tex
build/tracklength.tex: build/table_averaged-measurements.tex
build/framerate.tex: build/tracklength.tex
build/mass_ball.tex: build/framerate.tex
build/radius_ball.tex: build/mass_ball.tex
build/theoretical-I_ball.tex: build/radius_ball.tex
build/mass_cylinder.tex: build/theoretical-I_ball.tex
build/radius-inner_cylinder.tex: build/mass_cylinder.tex
build/radius-outer_cylinder.tex: build/radius-inner_cylinder.tex
build/theoretical-I_cylinder.tex: build/radius-outer_cylinder.tex

# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/v16516.pdf: build/plot-g_ball.pdf
build/v16516.pdf: build/parameter-g_ball.tex
build/v16516.pdf: build/parameter-t0-g_ball.tex
build/v16516.pdf: build/plot-g_cylinder.pdf
build/v16516.pdf: build/parameter-g_cylinder.tex
build/v16516.pdf: build/parameter-t0-g_cylinder.tex
build/v16516.pdf: build/plot-I_ball.pdf
build/v16516.pdf: build/parameter-I_ball.tex
build/v16516.pdf: build/parameter-t0-I_ball.tex
build/v16516.pdf: build/plot-I_cylinder.pdf
build/v16516.pdf: build/parameter-I_cylinder.tex
build/v16516.pdf: build/parameter-t0-I_cylinder.tex
build/v16516.pdf: build/framerate.tex
build/v16516.pdf: build/theoretical-I_ball.tex
build/v16516.pdf: build/theoretical-I_cylinder.tex
build/v16516.pdf: build/tracklength.tex
build/v16516.pdf: build/mass_ball.tex
build/v16516.pdf: build/mass_cylinder.tex
build/v16516.pdf: build/radius_ball.tex
build/v16516.pdf: build/radius-inner_cylinder.tex
build/v16516.pdf: build/radius-outer_cylinder.tex
build/v16516.pdf: build/table_all-measurements.tex
build/v16516.pdf: build/table_averaged-measurements.tex

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
