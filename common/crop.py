#!/usr/bin/env python3

import os
import subprocess
import sys
from shlex import join

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} in.crop out.pdf")
    exit(1)

pdfcrop = os.path.dirname(os.path.abspath(__file__)) + "/pdfcrop2.pl"

stem = sys.argv[1]
in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file) as f:
    s = f.read()
    s = s.splitlines()

source = s[0]
page = s[1]
box = s[2]

auto = True
if len(s) > 3:
    flags = s[3]
    flags = flags.split()
    auto = "noauto" not in flags

cmd0 = ["pdfseparate", "-f", page, "-l", page, source, out_file]
print(join(cmd0))
p = subprocess.run(cmd0, stdout=subprocess.PIPE)
cmd1 = ["perl", pdfcrop, "--mode", "absolute", "--margins", box, out_file, out_file]
print(join(cmd1))
p = subprocess.run(cmd1, stdout=subprocess.PIPE)
if auto:
    cmd2 = ["perl", pdfcrop, out_file, out_file]
    print(join(cmd2))
    p = subprocess.run(cmd2, stdout=subprocess.PIPE)
