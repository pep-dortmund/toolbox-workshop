include ../common/common.mk

FIGURES := $(addprefix build/figures/, $(addsuffix .pdf, os programming interest))

build/intro.pdf: $(FIGURES) $(addprefix build/figures/, matplotlib.png sympy.png scipy.png numpy.png)

$(FIGURES): script/answers.py data/answers.tsv
	python3 $<

build/figures/matplotlib.png: | build/figures
	wget https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Matplotlib_logo.svg/500px-Matplotlib_logo.svg.png -O $@ --no-use-server-timestamps

build/figures/sympy.png: | build/figures
	wget http://docs.sympy.org/latest/_static/sympylogo.png -O $@ --no-use-server-timestamps

build/figures/scipy.png: | build/figures
	wget https://raw.githubusercontent.com/scipy/scipy-sphinx-theme/master/_static/scipyshiny_small.png -O $@ --no-use-server-timestamps

build/figures/numpy.png: | build/figures
	wget http://www.numpy.org/_static/numpy_logo.png -O $@ --no-use-server-timestamps
