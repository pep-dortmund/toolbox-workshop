import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from collections.abc import Iterable

@dataclass    
class Templateline:
    linenumber: int
    line: str
    step_range: Iterable
    
    def __str__(self):
        return f"{self.linenumber:>3} {self.line}"



STEPRANGEREGEX = re.compile(r"(?:#|%)\s<(\d*)(-(\d*)|)>")

def setup_arg_parser():
    parser = argparse.ArgumentParser(
                    prog="generate-step-scripts",
                    description="Generate multiple files with lines from a template file",
                    epilog='')

    parser.add_argument('-v', '--verbose', action='store_true') 
    parser.add_argument('-n', '--dry-run', action='store_true') 
    parser.add_argument('-s', '--start-step', type=int)
    parser.add_argument('-t','--template_filepath', dest='template_filepath', required=True)           
    parser.add_argument('-o', '--output_filepaths', dest='output_filepaths', action="append", required=True)
    return parser                    

def parse_lines_and_stepranges(lines, max_upper_limit):
    #step_ranges = []
    script_lines = []
    removed_lines = []
    for i,l in enumerate(lines, start=1):
        found = STEPRANGEREGEX.search(l)
        if found is None: 
            removed_lines.append(Templateline(i,l, (None,  None)))
            continue
        groups = found.groups()

        lower_limit = int(groups[0])
        if (not groups[1]) and (groups[2] is None):
             step_limits = (lower_limit, lower_limit + 1)
        elif not groups[2]:
            step_limits = (lower_limit, max_upper_limit + 1)
        else:
            step_limits = (lower_limit, int(groups[2]) + 1)
        script_lines.append(Templateline(i, STEPRANGEREGEX.sub("", l).rstrip(), range(*step_limits)))

    return script_lines, removed_lines


def generate_step_file_lines(script_lines):
    step_files_lines = defaultdict(list)
    for line in script_lines:
         
        for step in line.step_range:
            step_files_lines[step].append(line)
    
    return step_files_lines


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
        template_lines = fh.readlines()

    script_lines, removed_lines = parse_lines_and_stepranges(template_lines, len(output_filepaths)) 

    step_files_lines = generate_step_file_lines(script_lines)

    if args.verbose:
        print("Removed lines:")
        print(f"{'\n'.join(str(rl) for rl in removed_lines)}")
        print(f"Found steps: {step_files_lines.keys()}")

    if args.dry_run:
        for step,lines in step_files_lines.items():
            print(f"\nOutputfile '{output_filepaths[map_step(step)-1]}' (Step: {step}) would these lines from the template file:")
            print(f"{"\n".join(str(l) for l in lines)}")
        return 


    try:
        for step, lines in step_files_lines.items():

            with open(output_filepaths[map_step(step)-1], "w") as fh:
                fh.write("\n".join(l.line for l in lines).strip())
    except IndexError: 
        raise ValueError(f"Expecting {max(step_files_lines.keys())} output files, but got only {len(output_filepaths)}.") 

if __name__ == "__main__":
    main()
