all:

include ../common/recursive.mk

all: $(BUILDS)
	@rm -rf build
	@mkdir -p build/exercises-toolbox-{1,2,3,4,5}
	@cp -r 1-python 2-numpy build/exercises-toolbox-1
	@cp -r 3-matplotlib 4-uncertainties build/exercises-toolbox-2
	@cp -r 5-make build/exercises-toolbox-3
	@cp -r 6-git build/exercises-toolbox-4
	@cp -r 7-all build/exercises-toolbox-5
	@rm -rf build/exercises-toolbox-{1,2,3,4,5}/*/{{,*/}{Makefile,.gitignore},*/__pycache__}
	@cd build ; \
	for day in 1 2 3 4 5 ; do \
		echo zip -rq exercises-toolbox-$$day.zip exercises-toolbox-$$day ; \
		zip -rq exercises-toolbox-$$day.zip exercises-toolbox-$$day ; \
	done

clean:
	git clean -Xdf

.PHONY: all clean
