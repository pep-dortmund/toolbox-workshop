#!/usr/bin/env python3

import os.path
import re
import sys

logfile = open(sys.argv[1], "r")
lines = [line.rstrip("\n") for line in logfile.readlines()]

re_file_page  = re.compile(r'^ ?((\)|\(([^ ")]+|"[^"]+")|\[[0-9]*|\]|<[^>]*>|\{[^}]*\}|\((using write cache|using read cache|load luc): [^)]*\)|ABD: EveryShipout initializing macros|luatex-hyphen: using data file: ([^ ")]+|"[^"]+")|luatex-hyphen: info: no hyphenation exceptions for this language|at position [0-9]+ in \'luaotfload.patch_font\'|luaotfload \| db : Font names database loaded from [^(]+|luaotfload \| load : Lookup/name: [^(]+) ?)+$')
re_file_page_interesting = re.compile(r'\)|\((?:[^ ")]+|"[^"]+")|\[[0-9]+|\]')

re_latex_error = re.compile(r'^! ')
re_latex_error_line = re.compile(r'^l\.([0-9]+) ')

re_latex_warning = re.compile(r'^LaTeX Warning: ')
re_latex_warning_undefined_reference = re.compile(r"^LaTeX Warning: Reference `([^']+)' on page [0-9]+ undefined on input line ([0-9]+)\.$")
re_latex_warning_undefined_references = r'LaTeX Warning: There were undefined references.'
re_latex_warning_multiple_label = re.compile(r"^LaTeX Warning: Label `([^']+)' multiply defined\.$")
re_latex_warning_multiple_labels = r'LaTeX Warning: There were multiply-defined labels.'
re_latex_warning_rerun = r'LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.'

re_latex_info = re.compile(r'^LaTeX ([^ ]+ )?Info: ')

re_package_warning = re.compile(r'^Package ([^ ]+) Warning: ')
re_package_rerunfilecheck_warning_rerun = re.compile(r"^Package rerunfilecheck Warning: File `[^']+' has changed.$")
re_package_biblatex_warning_rerun = re.compile('^Package biblatex Warning: Please \(re\)run Biber on the file:$')

re_package_info = re.compile(r'^Package ([^ ]+) Info: ')

re_latex3_error = r'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
re_latex3_error_end = r'|...............................................'
re_latex3_error_print_ignore = [
        r'! For immediate help type H <return>.',
        r'!...............................................',
        r"|'''''''''''''''''''''''''''''''''''''''''''''''",
        ]

re_latex3_warning = r'*************************************************'
re_latex3_warning_ignore = [
        r'LaTeX warning: "xparse/redefine-command"',
        r'LaTeX warning: "xparse/redefine-environment"',
        r'unicode-math warning: "mathtools-overbracket"',
        ]

re_latex3_info = r'.................................................'

re_full_box = re.compile(r'^(?:Over|Under)full \\(?:h|v)box')

files = list()
pages = [0]
page = None

def relativise_path(path):
    if not os.path.isabs(path):
        return path
    rel = os.path.relpath(os.path.abspath(path))
    return path if "../.." in rel else rel

def print_file_page(line=None):
    if line is None:
        print("{} (page {}):".format(relativise_path(files[-1]), pages[-1] + 1))
    else:
        print("{} (line {}, page {}):".format(relativise_path(files[-1]), line, pages[-1] + 1))

def print_latex_error(error):
    for line in error:
        print("  " + line)

latex_error = None

def print_package(package):
    for line in package[1]:
        print("  " + line)

package_warning = None
package_info = None

def print_latex3(latex3):
    for line in latex3[1:-1]:
        print("  " + line[2:])

def print_latex3_error(error):
    for line in error[2:-1]:
        if line not in re_latex3_error_print_ignore and line:
            if line[:2] == "l.":
                print("  " + line)
                print()
            else:
                print("  " + line[2:])

latex3_error = False
latex3_warning = False
latex3_info = False

exit_code = 0

for lineno, line in enumerate(lines):
    line = line.rstrip()
    if latex3_info is not False:
        latex3_info.append(line)
        if line == re_latex3_info:
            #print_file_page()
            #print_latex3(latex3_info)
            latex3_info = False
    elif latex3_warning is not False:
        latex3_warning.append(line)
        if line == re_latex3_warning:
            if latex3_warning[1][2:] not in re_latex3_warning_ignore:
                print_file_page()
                print_latex3(latex3_warning)
            latex3_warning = False
    elif latex3_error is not False:
        latex3_error.append(line)
        if line == re_latex3_error_end:
            print_file_page()
            print_latex3_error(latex3_error)
            latex3_error = False
    elif package_warning is not None and line.startswith(r'({}) '.format(package_warning[0])):
        package_warning[1].append(line)
        if not lines[lineno + 1].startswith(r'({}) '.format(package_warning[0])):
            print_file_page()
            print_package(package_warning)
            package_warning = None
    elif package_info is not None and line.startswith(r'({}) '.format(package_info[0])):
        package_info[1].append(line)
        if not lines[lineno + 1].startswith(r'({}) '.format(package_info[0])):
            #print_file_page()
            #print_package(package_info)
            package_info = None
    elif re_file_page.fullmatch(line) and re_file_page_interesting.findall(line):
        matches = re_file_page_interesting.findall(line)
        for match in matches:
            if match == ")" and len(files) > 1:
                files.pop()
            elif match[0] == "(":
                files.append(match[1:].strip('"'))
            elif match == "]":
                if page is not None:
                    pages.append(int(page))
                page = None
            elif match[0] == "[":
                page = match[1:]
    elif re_latex_error.match(line):
        latex_error = [line]
        if lineno == len(lines) - 1:
            print_file_page()
            print("  " + line)
    elif line == re_latex_warning_undefined_references or re_latex_warning_multiple_label.match(line) or line == re_latex_warning_multiple_labels:
        print(line)
    elif line == re_latex_warning_rerun:
        exit_code |= 2
        print(line)
    elif re_latex_warning_undefined_reference.match(line):
        match = re_latex_warning_undefined_reference.match(line)
        print_file_page(match.groups()[1])
        print("  LaTeX Warning: Reference `{}' undefined".format(match.groups()[0]))
    elif re_latex_warning.match(line):# or re_latex_info.match(line):
        print_file_page()
        print("  " + line)
    elif re_package_rerunfilecheck_warning_rerun.match(line):
        exit_code |= 2
        match = re_package_warning.match(line)
        package_warning = match.groups()[0], [line]
        if not lines[lineno + 1].startswith(r'({}) '.format(package_warning[0])):
            print_file_page()
            print("  " + line)
            package_warning = None
    elif re_package_biblatex_warning_rerun.match(line):
        exit_code |= 4
        match = re_package_warning.match(line)
        package_warning = match.groups()[0], [line]
        if not lines[lineno + 1].startswith(r'({}) '.format(package_warning[0])):
            print_file_page()
            print("  " + line)
            package_warning = None
    elif re_package_warning.match(line):
        match = re_package_warning.match(line)
        package_warning = match.groups()[0], [line]
        if not lines[lineno + 1].startswith(r'({}) '.format(package_warning[0])):
            print_file_page()
            print("  " + line)
            package_warning = None
    elif re_package_info.match(line):
        match = re_package_info.match(line)
        package_info = match.groups()[0], [line]
        if not lines[lineno + 1].startswith(r'({}) '.format(package_info[0])):
            #print_file_page()
            #print("  " + line)
            package_info = None
    elif re_full_box.match(line):
        print_file_page()
        print("  " + line)
        if "paragraph" in line:
            print("  " + lines[lineno + 1])
    elif line == re_latex3_info:
        latex3_info = [line]
    elif line == re_latex3_warning:
        latex3_warning = [line]
    elif line == re_latex3_error:
        latex3_error = [line]
    elif latex_error is not None:
        if re_latex_error_line.match(line):
            latex_error.append(line)
            match = re_latex_error_line.match(line)
            print_file_page(match.groups()[0])
            print_latex_error(latex_error)
            latex_error = None
        elif len(latex_error) < 4 and lineno < len(lines) - 1:
            latex_error.append(line)
        else:
            print_file_page()
            print("  " + latex_error[0])
            latex_error = None

sys.exit(exit_code)
