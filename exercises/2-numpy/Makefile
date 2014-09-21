all: $(addsuffix /loesung.pdf, 4-curve_fit 5-peakdetect 7-beugung)

%/loesung.pdf: %/loesung.py
	cd $* && python loesung.py
