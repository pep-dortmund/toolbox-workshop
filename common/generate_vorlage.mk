FILES := $(sort $(wildcard */loesung*.py))

define gen_vorlage = 
	grep -q '# begin solution' $(1) && : >$(dir $1)vorlage.py
	@[ ! -f "$(dir $1)vorlage.py" ] || cp $(1) $(dir $1)vorlage.py
	@[ ! -f "$(dir $1)vorlage.py" ] || sed -i -e '/# begin solution/,/# end solution/d' $(dir $1)vorlage.py
	@[ -s "$(dir $1)vorlage.py" ] || rm "$(dir $1)vorlage.py"
endef 

all: $(FILES)
	$(foreach loesung, $(FILES), $(call gen_vorlage,$(loesung));)
