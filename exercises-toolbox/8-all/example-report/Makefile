datafilenames = Messwerte_Bahn.txt \
Messwerte_Frames_Kugel.txt \
Messwerte_Frames_Zylinder.txt \
Messwerte_Kamera.txt \
Messwerte_Kugel.txt \
Messwerte_Zylinder.txt 

datafiles_without_unc = $(addprefix templates/data_without_uncertainties/, $(datafilenames))
datafiles_with_unc = $(addprefix templates/data_with_uncertainties/, $(datafilenames))


steps_without_unc = 1 2 3 4
steps_with_unc = 5 6 
steps = $(steps_without_unc) $(steps_with_unc)

taskfiles = $(foreach step, $(steps), $(addprefix templates/, aufgabe-step-$(step).txt))

step_dirs = $(foreach step, $(steps),build/report-example-step-$(step)/)
solution_dirs = $(addsuffix loesung, $(step_dirs))
data_dirs = $(addsuffix /data, $(solution_dirs))

target_datafiles_paths = $(addprefix build/report-example-step-STEP/loesung/data/, $(datafilenames))
target_datafiles_without_unc = $(foreach step, $(steps_without_unc), $(subst STEP,$(step), $(target_datafiles_paths)))
target_datafiles_with_unc = $(foreach step, $(steps_with_unc), $(subst STEP,$(step), $(target_datafiles_paths)))
datafiles_template_step-1 = $(addprefix build/report-example-step-1/data/, $(datafilenames)) 


target_makefiles = $(addsuffix Makefile-loesung, $(step_dirs))
target_scriptfiles = $(addsuffix loesung/auswertung.py, $(step_dirs))
target_taskfiles = $(addsuffix aufgabe.txt, $(step_dirs))
target_datafiles = $(datafiles_template_step-1) $(foreach step, $(steps), $(addprefix $(word $(step), $(solution_dirs))/data/, $(datafilenames)))



all: \
$(target_datafiles) \
$(target_taskfiles) \
$(target_scriptfiles) \


tests = test1 test2 test3
test-%: | build
	@echo " "
	@echo $@
	@echo " "
	@echo $<
	@echo " "
	@echo $(target_scriptfiles)
	@echo $(target_datafiles_without_unc)
	@echo $(target_datafiles_with_unc)
	@echo ""
	@echo $(subst STEP,1, $(target_datafiles_paths)) 

build/report-example-step-%/aufgabe.txt &: $(taskfiles) | $(solution_dirs)
	cp $(word $*, $(taskfiles)) build/report-example-step-$*/aufgabe.txt


build/report-example-step-%/Makefile-loesung &: templates/Makefile-loesung | $(solution_dirs)
	cp templates/Makefile-loesung build/report-example-step-$*/Makefile-loesung


$(target_scriptfiles) &: generate-step-scripts.py auswertung_template | $(solution_dirs)
	touch $(word 1, $(target_scriptfiles))
	python generate-step-scripts.py auswertung_template $(target_scriptfiles)

$(datafiles_template_step-1) &: | build/report-example-step-1
	cp -r templates/data_without_uncertainties build/report-example-step-1/data 

$(subst STEP,1, $(target_datafiles_paths)) &: $(datafiles_without_unc) | $(word 1, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 1, $(data_dirs))

$(subst STEP,2, $(target_datafiles_paths)) &: $(datafiles_without_unc) | $(word 2, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 2, $(data_dirs))

$(subst STEP,3, $(target_datafiles_paths)) &: $(datafiles_without_unc) | $(word 3, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 3, $(data_dirs))

$(subst STEP,4, $(target_datafiles_paths)) &: $(datafiles_without_unc) | $(word 4, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 4, $(data_dirs))

$(subst STEP,5, $(target_datafiles_paths)) &: $(datafiles_with_unc) | $(word 5, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 5, $(data_dirs))

$(subst STEP,6, $(target_datafiles_paths)) &: $(datafiles_with_unc) | $(word 6, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 6, $(data_dirs))


# $(target_datafiles_with_unc) &: $(datafiles_without_unc) | $(solution_dirs)
# 	cp -r templates/data_with_uncertainties $(target_datafiles_with_unc) 

build/report-example-step-%/loesung &:  | $(step_dirs) 
	mkdir -p build/report-example-step-$*/loesung


build/report-example-step-% : | build
	mkdir -p build/report-example-step-$*	

build:
	mkdir -p build

clean:
	rm -r build


# development rules

test_step_scripts: all
	@echo 
	@echo Testing: 
	@echo -n $(target_scriptfiles)
	@echo ""
	echo "" > build/output.txt 
	set -- $(solution_dirs); \
	for i do\
		cd "$$i"; \
		echo "Output of '$$i/auswertung.py':" >> ../../output.txt; \
		echo >> ../../output.txt; \
		echo "" >> ../../output.txt; \
		python auswertung.py >> ../../output.txt  2>&1;\
		cd - ;\
		echo $$(pwd) ; \
	done;\
	diff -u templates/steps_output.txt build/output.txt



.PHONY: all clean
