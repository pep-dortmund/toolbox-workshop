FILES := $(sort $(wildcard */loesung*.py))

all: $(addsuffix .dummy, $(FILES))

%.dummy: %
	cd $(dir $*) && python $(notdir $*)
	@touch $@
