include ../common/common.mk

build/figures/tex-overview.pdf: | build/figures
	cp "$$(texdoc -l -M tex-overview.pdf | awk -F $$'\t' '{ print $$3 }')" build/figures/tex-overview.pdf

$(addprefix build/figures/, $(addsuffix .pdf, engines-few engines-many formats-few formats-many)): build/figures/tex-overview.pdf

build/latex.pdf: $(addprefix build/figures/, $(addsuffix .pdf, $(basename $(shell ls -1 figures | grep '.crop$$'))))
