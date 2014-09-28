all: linleastsquares.pdf loesung.pdf daten.txt

daten.txt loesung.pdf: loesung.py
	python loesung.py

linleastsquares.pdf: linleastsquares.tex
	mkdir -p build
	lualatex --output-directory=build linleastsquares
	lualatex --output-directory=build linleastsquares
	mv build/linleastsquares.pdf .
	rm -r build
