all: build/plot.pdf build/parameter.txt

build/plot.pdf build/parameter.txt: auswertung.py lambda.txt L.txt I.txt | build
	python auswertung.py

build:
	mkdir -p build

clean: 
	rm -rf build

.PHONY: all clean
