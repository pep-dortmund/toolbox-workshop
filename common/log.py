#!/usr/bin/env python3

import os.path
import re
import sys

logfile = open(sys.argv[1], "r", encoding="utf8", errors="replace")
lines = [line.rstrip("\n") for line in logfile.readlines()]
lines.reverse()

def parse_path_page(lines):
    global paths, pages, page
    parts = [
            r'\)',
            r'\(([^ "()]+|"[^"]+")',
            r'\[[0-9]*',
            r'\]',
            r'<[^>]*>',
            r'\{[^}]*\}',
            r'\((using write cache|using read cache|load luc): [^)]*\)',
            r'ABD: EveryShipout initializing macros',
            r'luatex-hyphen: using data file: ([^ ")]+|"[^"]+")',
            r'luatex-hyphen: info: no hyphenation exceptions for this language',
            r'luatex-hyphen: loading patterns and exceptions for: [^ ]+ \([^)]+\)',
            r'(Inserting (`|\')[^\']+\' )?at position [0-9]+ in (`|\')[^\']+\'\.?',
            r'luaotfload \| db : Font names database loaded from [^(]+',
            r'luaotfload \| load : Lookup/name: [^(]+',
            r'Lua module: [^()[\]]+',
            ]
    if not re.match(r'^ ?(({}) ?)+$'.format('|'.join(parts)), lines[-1]):
        return None
    line = lines.pop()
    for match in re.findall(r'\)|\((?:[^ "()]+|"[^"]+")|\[[0-9]+|\]', line):
        if match == ")":# and len(paths) > 1: # should not happen
            paths.pop()
        elif match[0] == "(":
            paths.append(match[1:].strip('"'))
        elif match == "]":
            if page is not None: # this can happen: there are also empty []
                pages.append(int(page))
            page = None
        elif match[0] == "[":
            page = match[1:]
    return False

def parse_latex2_error(lines):
    match = re.match(r'^! (?:LaTeX|Class|Package) (?:([^ ]+) )?Error: ', lines[-1])
    if not match:
        return None
    message = [lines.pop()]
    empties = 0
    while empties < 2:
        line = lines.pop()
        if not line:
            empties += 1
        if line.rstrip() == " ...":
            message.pop() # See the first-argument package documentation for explanation.
            message.pop() # Type  H <return>  for immediate help.
            message.pop() # empty
        else:
            message.append(line)
    message.pop()
    return {
            "type": "latex2/error",
            "message": message,
            }

def parse_latex2(lines):
    match = re.match(r'^(?:LaTeX|Class|Package) (?:([^ ]+) )?(Warning|Info): ', lines[-1])
    if not match:
        return None
    if match.groups()[0]:
        continuation = "({})".format(match.groups()[0])
    else:
        continuation = " " * len(match.string[match.start():match.end()]) # LaTeX (Warning|Info)
    message = [lines.pop()]
    while lines[-1].startswith(continuation):
        message.append(lines.pop())
    return {
            "type": "latex2/" + match.groups()[1].lower(),
            "message": message,
            }

def parse_latex3_error(lines):
    if lines[-1] != r'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!':
        return None
    lines.pop()
    lines.pop()
    message = []
    while lines[-1]:
        line = lines.pop()
        if line.rstrip() == "!...............................................":
            message.pop() # For immediate help type H <return>.
            message.pop() # empty
            continue
        if line in [
                "|'''''''''''''''''''''''''''''''''''''''''''''''",
                "|..............................................."
                ]:
            continue
        if line[:2] in ["! ", "| "]:
            line = line[2:]
        message.append(line)
    return {
            "type": "latex3/error",
            "message": message,
            }

def parse_latex3(lines):
    types = {
            r'*************************************************': "warning",
            r'.................................................': "info",
            }
    if lines[-1] not in types:
        return None
    line = lines.pop()
    message = []
    while lines[-1] != line:
        message.append(lines.pop()[2:])
    lines.pop()
    return {
            "type": "latex3/" + types[line],
            "message": message,
            }

def parse_tex_error(lines):
    if not re.match(r'^!', lines[-1]):
        return None
    message = [lines.pop()]
    while lines and lines[-1]:
        message.append(lines.pop())
    return {
            "type": "tex/error",
            "message": message,
            }

def parse_box(lines):
    if not re.match(r'^(?:Over|Under)full \\(?:h|v)box', lines[-1]):
        return None
    message = [lines.pop()]
    if "paragraph" in message[0]:
        message.append(lines.pop())
    return {
            "type": "box",
            "message": message,
            }

paths = []
pages = [0]
page = None
messages = []

parsers = [
        parse_path_page,
        parse_latex2_error,
        parse_latex2,
        parse_latex3_error,
        parse_latex3,
        parse_tex_error,
        parse_box,
        ]

while lines:
    for parser in parsers:
        message = parser(lines)
        if message:
            message["path"] = paths[-1] if len(paths) else None
            message["page"] = pages[-1] + 1
            messages.append(message)
        if message is not None:
            break
    else:
        lines.pop()

if paths:
    print('log.py: paths non-empty: ' + str(paths))
if page:
    print('log.py: page non-None: ' + str(page))

def filter_info(message):
    if message["type"].endswith("/info"):
        return None
    return message

def filter_unicode_math_mathtools(message):
    if message["type"] == "latex3/warning" and message["message"][0] in [
            r'unicode-math warning: "mathtools-colon"',
            r'unicode-math warning: "mathtools-overbracket"',
            ]:
        return None
    return message

def filter_biblatex_footnotes(message):
    if message["type"] == "latex2/warning" and message["message"][0] == r'Package biblatex Warning: Patching footnotes failed.':
        return None
    return message

def filter_latex2_rerun_tex(message):
    global exit_code
    warnings = [
            r'^LaTeX Warning: Label\(s\) may have changed\. Rerun to get cross-references right\.$',
            r"^Package rerunfilecheck Warning: File `[^']+' has changed\.( Rerun\.)?$",
            r'^Package biblatex Warning: Please rerun LaTeX\.$',
            ]
    if message["type"] == "latex2/warning" and any(re.match(warning, message["message"][0]) for warning in warnings):
        exit_code |= 2
    return message

def filter_biblatex_rerun_biber(message):
    global exit_code
    if message["type"] == "latex2/warning" and message["message"][0] == r'Package biblatex Warning: Please (re)run Biber on the file:':
        exit_code |= 4
    return message

def filter_csquotes_polyglossia(message):
    if message["type"] == "latex2/warning" and message["message"][0] == "Package csquotes Warning: Using preliminary 'polyglossia' interface.":
        return None
    return message

def filter_caption_compatibility(message):
    if message["type"] == "latex2/warning" and message["message"][0] == "Package caption Warning: Forced redefinition of \caption since the":
        return None
    return message

exit_code = 0

filters = [
        filter_info,
        filter_unicode_math_mathtools,
        filter_biblatex_footnotes,
        filter_latex2_rerun_tex,
        filter_biblatex_rerun_biber,
        filter_csquotes_polyglossia,
        filter_caption_compatibility,
        ]

messages_copy = list(messages)
messages = []
for message in messages_copy:
    for filt in filters:
        message = filt(message)
        if not message:
            break
    else:
        messages.append(message)

def relativise_path(path):
    if path.startswith('./'):
        path = path[2:]
    if not os.path.isabs(path):
        return path
    rel = os.path.relpath(os.path.abspath(path))
    return path if "../.." in rel else rel

for message in messages:
    if message["path"] is not None:
        print(relativise_path(message["path"]), end="")
        if message["page"] is not None:
            print(" (page {})".format(message["page"]), end="")
        print(":")
        indent = "  "
    else:
        indent = ""
    for line in message["message"]:
        print(indent, line)

sys.exit(exit_code)
