all: $(addsuffix /loesung.pdf, 5-curve_fit 6-peakdetect 7-beugung)

%/loesung.pdf: %/loesung.py
	cd $* && python loesung.py
