include ../../common/common.mk
include ../../common/loesung.py.mk
include ../../common/generate_vorlage.mk

all: 5-readwrite/test.txt example-report/v16516.pdf

5-readwrite/test.txt: 5-readwrite/loesung2.py.dummy
	@echo "Dies ist ein Beispiel" > 5-readwrite/test.txt

example-report/v16516.pdf: | ../8-all/report-example/loesung/v16516/build/v16516.pdf 
	cp ../8-all/report-example/loesung/v16516/build/v16516.pdf example-report

../8-all/report-example/loesung/v16516/build/v16516.pdf:
		$(MAKE) -C ../8-all/report-example/loesung/v16516/ 
