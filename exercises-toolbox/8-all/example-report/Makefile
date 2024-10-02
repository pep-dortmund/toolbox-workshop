datafilenames = Messwerte_Bahn.txt \
Messwerte_Frames_Kugel.txt \
Messwerte_Frames_Zylinder.txt \
Messwerte_Kamera.txt \
Messwerte_Kugel.txt \
Messwerte_Zylinder.txt 

datafiles_without_unc = $(addprefix templates/data_without_uncertainties/, $(datafilenames))
datafiles_with_unc = $(addprefix templates/data_with_uncertainties/, $(datafilenames))


steps_without_unc = 1 2 3 4
steps_with_unc = 5 6 7 8 9 10
steps_with_latex = 7 8 9 10

steps = $(steps_without_unc) $(steps_with_unc)

template_taskfiles = $(foreach step, $(steps), $(addprefix templates/, aufgabe-step-$(step).txt))
template_bibfiles = $(addprefix templates/, lit.bib programme.bib)

step_dirs = $(foreach step, $(steps),build/report-example-step-$(step)/)
solution_dirs = $(addsuffix loesung/, $(step_dirs))
data_dirs = $(addsuffix data, $(solution_dirs))

step_dirs_with_latex = $(foreach step, $(steps_with_latex),build/report-example-step-$(step)/)
solution_dirs_with_latex = $(addsuffix loesung/, $(step_dirs_with_latex))
content_dirs_with_latex = $(addsuffix content/, $(solution_dirs_with_latex))

target_datafiles_paths = $(addprefix build/report-example-step-$(1)/loesung/data/, $(datafilenames))
datafiles_template_step-1 = $(addprefix build/report-example-step-1/data/, $(datafilenames)) 
datafiles_template_step-5 = $(addprefix build/report-example-step-5/data/, $(datafilenames)) 


target_taskfiles = $(addsuffix aufgabe.txt, $(step_dirs))
target_datafiles = $(datafiles_template_step-1) $(datafiles_template_step-5) $(foreach step, $(steps), $(addprefix $(word $(step), $(solution_dirs))data/, $(datafilenames)))

target_makefiles = $(addsuffix Makefile-loesung, $(step_dirs))

target_pythonfiles = $(addsuffix auswertung.py, $(solution_dirs))

target_texfiles_v16516 = $(addsuffix v16516.tex, $(solution_dirs_with_latex))
target_texfiles_header = $(addsuffix header.tex, $(solution_dirs_with_latex))
target_texfiles_durchfuehrung = $(addsuffix content/durchfuehrung.tex, $(solution_dirs_with_latex))
target_texfiles_theorie = $(addsuffix content/theorie.tex, $(solution_dirs_with_latex))
target_texfiles_auswertung = $(addsuffix content/auswertung.tex, $(solution_dirs_with_latex))
target_texfiles_diskussion = $(addsuffix content/diskussion.tex, $(solution_dirs_with_latex))
target_bibfiles = $(addsuffix lit.bib, $(wordlist 3,4,$(solution_dirs_with_latex))) $(addsuffix programme.bib, $(wordlist 3,4,$(solution_dirs_with_latex)))




all: \
$(target_datafiles) \
$(target_taskfiles) \
$(target_pythonfiles) \
$(target_texfiles_header) \
$(target_texfiles_v16516) \
$(target_texfiles_durchfuehrung) \
$(target_texfiles_theorie) \
$(target_texfiles_auswertung) \
$(target_texfiles_diskussion) \
$(target_bibfiles)\


build/report-example-step-%/aufgabe.txt &: $(template_taskfiles) | $(solution_dirs)
	cp $(word $*, $(template_taskfiles)) build/report-example-step-$*/aufgabe.txt

$(target_bibfiles) &: $(template_bibfiles) | $(solution_dirs_with_latex)
	cp templates/lit.bib $(word 1, $(target_bibfiles))
	cp templates/lit.bib $(word 2, $(target_bibfiles))
	cp templates/programme.bib $(word 3, $(target_bibfiles))
	cp templates/programme.bib $(word 4, $(target_bibfiles))


build/report-example-step-%/Makefile-loesung &: templates/Makefile-loesung | $(solution_dirs)
	cp templates/Makefile-loesung build/report-example-step-$*/Makefile-loesung

$(target_texfiles_v16516) &: generate-step-files.py templates/latex/v16516_tex_template | $(solution_dirs_with_latex)
	python generate-step-files.py -t templates/latex/v16516_tex_template $(addprefix -o=,$(target_texfiles_v16516)) -s 7

$(target_texfiles_header) &: generate-step-files.py templates/latex/header_tex_template | $(solution_dirs_with_latex)
	python generate-step-files.py -t templates/latex/header_tex_template $(addprefix -o=,$(target_texfiles_header)) -s 7

$(target_texfiles_durchfuehrung) &: generate-step-files.py templates/latex/durchfuehrung_tex_template | $(content_dirs_with_latex)
	python generate-step-files.py -t templates/latex/durchfuehrung_tex_template $(addprefix -o=,$(target_texfiles_durchfuehrung)) -s 7
$(target_texfiles_theorie) &: generate-step-files.py templates/latex/theorie_tex_template | $(content_dirs_with_latex)
	python generate-step-files.py -t templates/latex/theorie_tex_template $(addprefix -o=,$(target_texfiles_theorie)) -s 7
$(target_texfiles_auswertung) &: generate-step-files.py templates/latex/auswertung_tex_template | $(content_dirs_with_latex)
	python generate-step-files.py -t templates/latex/auswertung_tex_template $(addprefix -o=,$(target_texfiles_auswertung)) -s 7
$(target_texfiles_diskussion) &: generate-step-files.py templates/latex/diskussion_tex_template | $(content_dirs_with_latex)
	python generate-step-files.py -t templates/latex/diskussion_tex_template $(addprefix -o=,$(target_texfiles_diskussion)) -s 7

$(target_pythonfiles) &: generate-step-files.py templates/auswertung_py_template | $(solution_dirs)
	touch $(word 1, $(target_pythonfiles))
	python generate-step-files.py -t templates/auswertung_py_template $(addprefix -o=, $(wordlist 2,10,$(target_pythonfiles))) -s 2

$(datafiles_template_step-1) &: | build/report-example-step-1
	cp -r templates/data_without_uncertainties build/report-example-step-1/data 

$(datafiles_template_step-5) &: | build/report-example-step-5
	cp -r templates/data_with_uncertainties build/report-example-step-5/data 

$(call target_datafiles_paths,1) &: $(datafiles_without_unc) | $(word 1, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 1, $(data_dirs))

$(call target_datafiles_paths,2) &: $(datafiles_without_unc) | $(word 2, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 2, $(data_dirs))

$(call target_datafiles_paths,3) &: $(datafiles_without_unc) | $(word 3, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 3, $(data_dirs))

$(call target_datafiles_paths,4) &: $(datafiles_without_unc) | $(word 4, $(solution_dirs))
	cp -r templates/data_without_uncertainties $(word 4, $(data_dirs))

$(call target_datafiles_paths,5) &: $(datafiles_with_unc) | $(word 5, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 5, $(data_dirs))

$(call target_datafiles_paths,6) &: $(datafiles_with_unc) | $(word 6, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 6, $(data_dirs))

$(call target_datafiles_paths,7) &: $(datafiles_with_unc) | $(word 7, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 7, $(data_dirs))

$(call target_datafiles_paths,8) &: $(datafiles_with_unc) | $(word 8, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 8, $(data_dirs))

$(call target_datafiles_paths,9) &: $(datafiles_with_unc) | $(word 9, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 9, $(data_dirs))

$(call target_datafiles_paths,10) &: $(datafiles_with_unc) | $(word 10, $(solution_dirs))
	cp -r templates/data_with_uncertainties $(word 10, $(data_dirs))

build/report-example-step-7/loesung/content &:  | $(solution_dirs) 
	mkdir -p build/report-example-step-7/loesung/content

build/report-example-step-8/loesung/content &:  | $(solution_dirs) 
	mkdir -p build/report-example-step-8/loesung/content

build/report-example-step-9/loesung/content &:  | $(solution_dirs) 
	mkdir -p build/report-example-step-9/loesung/content

build/report-example-step-10/loesung/content &:  | $(solution_dirs) 
	mkdir -p build/report-example-step-10/loesung/content

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
	@echo "auswertung.py"
	@echo ""
	echo "" > build/python_output.txt 
	set -- $(solution_dirs); \
	for i do\
		cd "$$i"; \
		echo "$$PWD"; \
		echo "Output of '$${i}auswertung.py':" >> ../../python_output.txt; \
		echo "" >> ../../python_output.txt; \
		python auswertung.py >> ../../python_output.txt;\
		cd - >> /dev/null; \
	done;\
	diff -u templates/output_snapshot.txt build/python_output.txt  && echo "Test Passed!: No changes in output of scripts"

#diff -u templates/output_snapshot.txt build/output.txt || diff -u templates/output_snapshot.txt build/output.txt   && echo "Test Passed!: No changes in output of scripts"



.PHONY: all clean
