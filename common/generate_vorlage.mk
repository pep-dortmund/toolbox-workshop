FILES := $(sort $(wildcard */loesung*.py))
targets := $(subst loesung,vorlage,$(FILES))


all: $(FILES) $(targets)
	# $(foreach (loesung,vorlage), ($(FILES), $(targets)), $(call gen_vorlage,$(loesung),$(vorlage));)

$(targets): %: ../../common/gen_vorlage.sh
	@echo $@
	bash $< $@
