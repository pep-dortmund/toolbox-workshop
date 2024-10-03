datafilenames = Messwerte_Bahn.txt \
Messwerte_Frames_Kugel.txt \
Messwerte_Frames_Zylinder.txt \
Messwerte_Kamera.txt \
Messwerte_Kugel.txt \
Messwerte_Zylinder.txt 

advanced_mpl_filenames = matplotlibrc header-matplotlib.tex

steps = 01 02 03 04 05 06 07 08 09 10 11

### Directories 

# build/example-report-step-{01,...,11}/
step_dirs = $(foreach step, $(steps),build/example-report-step-$(step)/)

# build/example-report-step-{01,...,11}/loesung
solution_dirs = $(addsuffix loesung/, $(step_dirs))


# build/example-report-step-{06,...,11}/loesung/v16516/
report_dirs = $(addsuffix v16516/, $(wordlist 6,11,$(solution_dirs)))

# build/example-report-step-{01,05}/data/
step_data_dirs = $(addsuffix data/, $(word 1,$(step_dirs)) $(word 5,$(step_dirs)))

# build/example-report-step-{01,...,05}/loesung/data/
solution_data_dirs = $(addsuffix data/, $(wordlist 1,5,$(solution_dirs)))

# build/example-report-step-{06,...,11}/loesung/v16516/data
report_data_dirs = $(addsuffix data/, $(report_dirs))

# all */data  dirs
data_dirs = $(solution_data_dirs) $(report_data_dirs) $(step_data_dirs)
data_dirs_without_unc = $(wordlist 1,4,$(data_dirs)) $(word 12,$(data_dirs))
data_dirs_with_unc = $(wordlist 5,11,$(data_dirs)) $(word 13,$(data_dirs))

# build/example-report-step-{09,...,10}/loesung/v16516/graphics/
graphics_dirs = $(addsuffix v16516/graphics/, $(wordlist 9,10,$(solution_dirs)))

# solution_dirs containing tex files
solution_dirs_with_tex = $(wordlist 7,11,$(solution_dirs))
#build/example-report-step-{07,...,11}/loesung/v16516/content/
content_dirs = $(addsuffix v16516/content/, $(solution_dirs_with_tex))

### Taskfiles

task_files = $(addsuffix aufgabe.txt,$(step_dirs))

### Datafiles

append_datafilenames = $(foreach filename,$(datafilenames),$(addsuffix $(filename), $(1)))

data_files_without_unc =  $(call append_datafilenames,$(data_dirs_without_unc))
data_files_with_unc = $(call append_datafilenames, $(data_dirs_with_unc))
data_files = $(data_files_without_unc) $(data_files_with_unc)

### Python files 
solution_python_files = $(addsuffix auswertung.py, $(wordlist 1,5,$(solution_dirs)))
report_python_files = $(addsuffix auswertung.py, $(report_dirs))
python_files = $(solution_python_files) $(report_python_files)

### LaTeX Files
header_tex_files=$(addsuffix header.tex, $(solution_dirs_with_tex))
main_tex_files= $(addsuffix v16516/v16516.tex, $(solution_dirs_with_tex))
implementation_tex_files=$(addsuffix durchfuehrung.tex, $(content_dirs))
theory_tex_files=$(addsuffix theorie.tex, $(content_dirs))
evaluation_tex_files=$(addsuffix auswertung.tex, $(content_dirs))
discussion_tex_files=$(addsuffix diskussion.tex, $(content_dirs))

setup_image_files = $(addsuffix versuchsaufbau.png, $(graphics_dirs))

lit_bib_files = $(addsuffix lit.bib, $(wordlist 9,11,$(solution_dirs)))
programms_bib_files = $(addsuffix programme.bib, $(wordlist 9,11,$(solution_dirs)))
bib_files = $(lit_bib_files) $(programms_bib_files)

matplotlibrc_files= $(addsuffix matplotlibrc, $(wordlist 10,11,$(solution_dirs)))
header_matplotlib_files = $(addsuffix header-matplotlib.tex, $(wordlist 10,11,$(solution_dirs)))

advanced_mpl_files = $(matplotlibrc_files) $(header_matplotlib_files)

tex_files = $(header_tex_files) \
						$(main_tex_files) \
						$(implementation_tex_files) \
						$(theory_tex_files) \
						$(evaluation_tex_files) \
						$(discussion_tex_files) \
						$(bib_files) \
						$(advanced_mpl_files) 

### Makefiles
solution_makefile_files = $(addsuffix Makefile-loesung, $(wordlist 2,5,$(solution_dirs))) \
													$(addsuffix v16516/Makefile-loesung, $(wordlist 6,9,$(solution_dirs)))

target_makefile_files = $(addsuffix v16516/Makefile, $(wordlist 10,11,$(solution_dirs)))
makefile_files = $(solution_makefile_files) $(target_makefile_files)




all:$(task_files) \
		$(python_files) \
		$(data_files) \
		$(tex_files) \
		$(setup_image_files) \
		$(makefile_files)


build/example-report-step-%/aufgabe.txt &: $(template_task_files) | $(step_dirs)
	cp templates/aufgabe-step-$*.txt build/example-report-step-$*/aufgabe.txt

copy_file_loop=set -- $(2); for i do cp $(1) $$i; done

$(solution_makefile_files) &: templates/Makefile-loesung_template | $(solution_dirs) $(report_dirs)
	python generate-step-files.py -t $< -s 2 $(addprefix -o=,$(solution_makefile_files))

$(target_makefile_files) &: templates/Makefile | $(report_dirs)
	$(call copy_file_loop, $<, $(target_makefile_files))

$(matplotlibrc_files) &: templates/matplotlibrc | $(solution_dirs)
	$(call copy_file_loop, $<,$(matplotlibrc_files))

$(programms_bib_files) &: templates/programme.bib | $(solution_dirs)
	$(call copy_file_loop, $<, $(programms_bib_files))

$(lit_bib_files) &: templates/lit.bib | $(solution_dirs)
	$(call copy_file_loop, $<, $(lit_bib_files))

$(setup_image_files) &: templates/versuchsaufbau.png | $(graphics_dirs)
	$(call copy_file_loop, $<, $(setup_image_files))

$(header_matplotlib_files) &: templates/header-matplotlib.tex | $(solution_dirs)
	$(call copy_file_loop, $<, $(header_matplotlib_files))

$(header_tex_files) &: templates/latex/header_tex_template | $(solution_dirs)
	python generate-step-files.py -t $< -s 7 $(addprefix -o=,$(header_tex_files))

$(main_tex_files) &: templates/latex/v16516_tex_template | $(content_dirs)
	python generate-step-files.py -t $< -s 7 $(addprefix -o=,$(main_tex_files))

$(theory_tex_files) &: templates/latex/theorie_tex_template | $(content_dirs)
	python generate-step-files.py -t $< -s 7 $(addprefix -o=,$(theory_tex_files))

$(implementation_tex_files) &: templates/latex/durchfuehrung_tex_template | $(content_dirs)
	python generate-step-files.py -t $< -s 7 $(addprefix -o=,$(implementation_tex_files))

$(evaluation_tex_files) &: templates/latex/auswertung_tex_template | $(content_dirs)
	python generate-step-files.py -t $< -s 7 $(addprefix -o=,$(evaluation_tex_files))

$(discussion_tex_files) &: templates/latex/diskussion_tex_template | $(content_dirs)
	python generate-step-files.py -t $< -s 7 $(addprefix -o=,$(discussion_tex_files))

$(python_files) &: templates/auswertung_py_template | $(solution_dirs) $(report_dirs)
	python generate-step-files.py -t templates/auswertung_py_template $(addprefix -o=,$(python_files))


copy_dir_loop=set -- $(2); for i do cp -r $(1) $$i; done
$(data_files_without_unc) &: templates/data_without_uncertainties/* | $(solution_dirs) $(report_dirs)
	$(call copy_dir_loop, templates/data_without_uncertainties, $(data_dirs_without_unc))
	
$(data_files_with_unc) &: templates/data_with_uncertainties/* | $(solution_dirs) $(report_dirs)
	$(call copy_dir_loop, templates/data_with_uncertainties, $(data_dirs_with_unc))

$(content_dirs) &:|$(report_dirs)
	mkdir -p $(content_dirs) 	

$(graphics_dirs)&: |$(report_dirs)
	mkdir -p $(graphics_dirs)

$(report_dirs)&: | $(solution_dirs) 
	mkdir -p $(report_dirs)

$(solution_dirs) &: | $(step_dirs)
	mkdir -p $(solution_dirs)

$(step_dirs): | build
	mkdir -p $(step_dirs)

build:
	mkdir -p build

clean:
	rm -r build

.PHONY: all clean

