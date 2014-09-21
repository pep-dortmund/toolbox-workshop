all: $(addsuffix /loesung.pdf, 1-curve_fit 2-peakdetect 4-beugung)

%/loesung.pdf: %/loesung.py
	cd $* && python loesung.py
