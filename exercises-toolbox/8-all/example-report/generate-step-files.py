import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from collections.abc import Iterable

STEPRANGEREGEX = re.compile(r"(?:#|%)\s*<(\d*)(-(\d*)|)>")

@dataclass    
class Templateline:
    linenumber: int
    line: str
    step_range: Iterable
    
    def __str__(self):
        return f"{self.linenumber:>3} {self.line}"


def setup_arg_parser():
    parser = argparse.ArgumentParser(
                    prog="generate-step-files",
                    description="Generate multiple (step)files containing lines from a template file",
                    epilog='')

    parser.add_argument('-v', '--verbose', action='store_true', 
                        help="Get info on parsed args, the step maximum steprange in the template and to be removed lines.") 
    parser.add_argument('-n', '--dry-run', action='store_true', 
                        help="Print the content of each output file to stdout instead of generating any files.") 
    # This option allows to use the same step numbering in differnt independent files
    parser.add_argument('-s', '--start-step', type=int, default=1,
                        help="Set the step that should be considered step 1 for this file")
    parser.add_argument('-t','--template_filepath', dest='template_filepath', required=True, 
                        help="Filepath to the template file.")           
    parser.add_argument('-o', '--output_filepaths', dest='output_filepaths', action="append", required=True, 
                        help="Filepaths to the output files (you need to use one Option -o <file> for each file). Hint: use -o=file{1,2,3} for example, to generate the multiple options.)")
    return parser                    

def parse_lines_and_stepranges(lines, max_upper_limit):
    #step_ranges = []
    template_lines = []
    removed_lines = []
    for i,l in enumerate(lines, start=1):
        found = STEPRANGEREGEX.search(l)
        
        # a line containing no pattern will not be saved to any output file, hence 'removed'
        if found is None: 
            removed_lines.append(Templateline(i,l, (None,  None)))
            continue
        groups = found.groups()
        
        try: 
            lower_limit = int(groups[0])
        except ValueError:
            raise ValueError(f"The pattern in line {i} of the template file has not starting step")
        
        # The dash and second number can be omitted:
        # e.g. <4> is equivalent to <4-4>
        if (not groups[1]) and (groups[2] is None):
            # The upper limit has to be increased by one to be inclusive as a range 
            step_limits = (lower_limit, lower_limit + 1)

        # If the second number is omitted but the dash is not, the upper limit is the last step: 
        # e.g. <4-> is equivalent to <4-10> if 10 output files are generated
        elif not groups[2]:
            step_limits = (lower_limit, max_upper_limit + 1)

        # both numbers are present in the pattern
        else:
            step_limits = (lower_limit, int(groups[2]) + 1)

        num_files_with_line = step_limits[1] - step_limits[0]
        if num_files_with_line > max_upper_limit:
            raise ValueError(f"The number of given output files is {max_upper_limit},"
            f" but line {i} of the template file is expected to appear in {num_files_with_line} output files (pattern: {found.group()}).") 
        
        # remove the steprange pattern and spaces between line content and pattern 
        line_content = STEPRANGEREGEX.sub("", l).rstrip() 
        template_lines.append(Templateline(i, line_content, range(*step_limits)))

    return template_lines, removed_lines


def split_stepfile_lines(template_lines, output_filepaths, start_step):
    # mapping the start_step to the first given output file
    map_first_step = lambda step: step - (start_step - 1)

    lines_per_stepfile = defaultdict(list)
    for line in template_lines:
        for step in line.step_range:
            lines_per_stepfile[output_filepaths[map_first_step(step)-1]].append(line)

    return lines_per_stepfile


def main():
    parser = setup_arg_parser()
    args = parser.parse_args()

    template_filepath = args.template_filepath
    output_filepaths = args.output_filepaths
    

    if args.verbose:
        print("Input:")
        print(' '.join(sys.argv))
        print("Parsed:")
        print(f" - template file: {template_filepath}")
        print(f" - output files: {output_filepaths}")
        print(f" - start step: {args.start_step}")

   
    with open(template_filepath) as fh:
        template_lines = fh.readlines()

    template_lines, removed_lines = parse_lines_and_stepranges(template_lines, len(output_filepaths)) 

    lines_per_stepfiles = split_stepfile_lines(template_lines, output_filepaths, args.start_step)

    if args.verbose:
        print("Removed lines:")
        print(f"{'\n'.join(str(rl) for rl in removed_lines)}")
        print(f"Found steps: {lines_per_stepfiles.keys()}")
    

    if args.dry_run:
        for stepfile, lines in lines_per_stepfiles.items():
            print(f"\nOutput file '{stepfile}' would these lines from the template file:")
            print(f"{"\n".join(str(l) for l in lines)}")
        return 


    for stepfile, lines in lines_per_stepfiles.items():
        with open(stepfile, "w") as fh:
            fh.write("\n".join(l.line for l in lines).strip())

if __name__ == "__main__":
    main()
