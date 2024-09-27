import argparse
import re
import sys
from collections import defaultdict

STEPRANGEREGEX = re.compile(r"(?:#|%)\s<(\d*)(-(\d*)|)>")

def parse_int_tuple(tuple_str):
    values = tuple_str.split(",")
    return (int(values[0]), int(values[1]))


def setup_arg_parser():
    parser = argparse.ArgumentParser(
                    prog="generate-step-scripts",
                    description="Generate multiple files with lines from a template file",
                    epilog='')

    parser.add_argument('-v', '--verbose', action='store_true') 
    parser.add_argument('-r', '--map-from-range',type=parse_int_tuple)
    parser.add_argument('-t','--template_filepath', dest='template_filepath')           
    parser.add_argument('-o', '--output_filepaths', dest='output_filepaths', action="append")
    return parser                    

def extract_stepranges(lines, max_upper_limit):
    step_ranges = []
    script_lines = []
    for l in lines:
        found = STEPRANGEREGEX.search(l)
        if found is None: 
            continue
        groups = found.groups()

        lower_limit = int(groups[0])
        if (not groups[1]) and (groups[2] is None):
             step_limits = (lower_limit, lower_limit + 1)
        elif not groups[2]:
            step_limits = (lower_limit, max_upper_limit + 1)
        else:
            step_limits = (lower_limit, int(groups[2]) + 1)
        step_ranges.append(range(*step_limits))
        script_lines.append(STEPRANGEREGEX.sub("", l).rstrip())

    return step_ranges, script_lines


def generate_step_file_lines(template_lines, num_output_files):
    step_ranges, script_lines = extract_stepranges(template_lines, num_output_files)
     
    files_lines = defaultdict(list)
    for sl, line in zip(step_ranges, script_lines):
        
        print(f"sl: {sl}: {line}")
        for step in sl:
            files_lines[step].append(line)
    

    return files_lines


def main():
    parser = setup_arg_parser()
    args = parser.parse_args()
    template_filepath = args.template_filepath
    output_filepaths = args.output_filepaths
    if args.verbose:
        print(f"Templatefile: {template_filepath}")
        print(f"Outputfiles: {output_filepaths}")
        print(f"range: {args.map_from_range}")

    
    


    with open(template_filepath) as fh:
        script_lines = fh.readlines()
    
    files_lines = generate_step_file_lines(script_lines, len(output_filepaths))

    if args.verbose:
        print(f"Found steps: {files_lines.keys()}")


    map_step = lambda step: step 
    if args.map_from_range:
        map_step = lambda step: step - args.map_from_range[0]

    try:
        for step, lines in files_lines.items():

            with open(output_filepaths[map_step(step)-1], "w") as fh:
                fh.write("\n".join(lines).strip())
    except IndexError: 
        raise ValueError(f"Expecting {max(files_lines.keys())} output files, but got only {len(output_filepaths)}.") 

if __name__ == "__main__":
    main()
