all: $(addsuffix .html, Python ScientificPython Matplotlib uncertainties)

%.html: %.ipynb
	jupyter-nbconvert --execute --allow-errors --to html $<

muon_plot.png: muon_plot.py muon_data.txt
	python3 $<
