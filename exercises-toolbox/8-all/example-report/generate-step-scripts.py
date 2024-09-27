import argparse
import re
import sys
from collections import defaultdict

STEPRANGEREGEX = re.compile(r"(?:#|%)\s<(\d*)(-(\d*)|)>")

def setup_arg_parser():
    parser = argparse.ArgumentParser(
                    prog="generate-step-scripts",
                    description="Generate multiple files with lines from a template file",
                    epilog='')

    parser.add_argument('-v', '--verbose', action='store_true') 
    parser.add_argument('-n', '--dry-run', action='store_true') 
    parser.add_argument('-s', '--start-step', type=int)
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
         
        for step in sl:
            files_lines[step].append(line)
    

    return files_lines


def main():
    parser = setup_arg_parser()
    args = parser.parse_args()
    template_filepath = args.template_filepath
    output_filepaths = args.output_filepaths
    if args.verbose:
        print("Input:")
        print(' '.join(sys.argv))
        print("Parsed:")
        print(f" - Templatefile: {template_filepath}")
        print(f" - Outputfiles: {output_filepaths}")
        print(f" - Start step: {args.start_step}")

    map_step = lambda step: step 
    if args.start_step:
        map_step = lambda step: step - (args.start_step - 1)
    
    


    with open(template_filepath) as fh:
        script_lines = fh.readlines()
    
    files_lines = generate_step_file_lines(script_lines, len(output_filepaths))

    if args.verbose:
        print(f"Found steps: {files_lines.keys()}")

    if args.dry_run:
        for step,lines in files_lines.items():
            print(f"\nOutputfile '{output_filepaths[map_step(step)-1]}' (Step: {step}) would contain:")
            print(f"{"\n".join(lines)}")
        return 


    try:
        for step, lines in files_lines.items():

            with open(output_filepaths[map_step(step)-1], "w") as fh:
                fh.write("\n".join(lines).strip())
    except IndexError: 
        raise ValueError(f"Expecting {max(files_lines.keys())} output files, but got only {len(output_filepaths)}.") 

if __name__ == "__main__":
    main()
