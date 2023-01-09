#!/usr/bin/env python3

import os
import subprocess
import sys

if len(sys.argv) < 3:
    print("Usage: {} in.crop out.pdf".format(sys.argv[0]))
    exit(1)

pdfcrop = os.path.dirname(os.path.abspath(__file__)) + "/pdfcrop2.pl"

stem = sys.argv[1]
in_file = sys.argv[1]
out_file = sys.argv[2]

s = open(in_file, "r").read()
s = s.splitlines()

source = s[0]
page = s[1]
box = s[2]

auto = True
if len(s) > 3:
    flags = s[3]
    flags = flags.split()
    auto = not "noauto" in flags

print(r"pdfseparate -f {0} -l {0} {1} {2}".format(page, source, out_file))
p = subprocess.Popen(["pdfseparate", "-f", page, "-l", page, source, out_file], stdout=subprocess.PIPE)
p.communicate()
print(r"pdfcrop2.pl --mode absolute --margins '{0}' {1} {1}".format(box, out_file))
p = subprocess.Popen(["perl", pdfcrop, "--mode", "absolute", "--margins", box, out_file, out_file], stdout=subprocess.PIPE)
p.communicate()
if auto:
    print(r"pdfcrop2.pl {0} {0}".format(out_file))
    p = subprocess.Popen(["perl", pdfcrop, out_file, out_file], stdout=subprocess.PIPE)
    p.communicate()
