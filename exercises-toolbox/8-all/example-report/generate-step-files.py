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
    outputfile_index_range: Iterable
    pattern: str
    
    def __str__(self):
        pattern_length = len(self.pattern)
        # magic number 10: the amount of padding necessary to print a pattern with two two-digit numbers
        return f"({self.pattern}) {" "*(10-pattern_length)} {self.linenumber:>3} {self.line}"


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

def parse_lines_and_stepranges(lines, start_step, end_step):
    template_lines = []
    removed_lines = []
    for i,l in enumerate(lines, start=1):
        found = STEPRANGEREGEX.search(l)
        
        # a line containing no pattern will not be saved to any output file, hence 'removed'
        if found is None: 
            removed_lines.append(Templateline(i,l, (None,  None), ""))
            continue
        groups = found.groups()
        
        try: 
            lower_step_limit = int(groups[0])
        except ValueError:
            raise ValueError(f"The pattern ({found.group()}) in line {i} of the template file has not starting step.")
        if lower_step_limit > end_step:
            raise ValueError(f"The number of output filepaths ({end_step}) is lower then the lower limit in the pattern '{found.group()}' in line {i} of the template file.")
       
        # Since the end_step is calculated from the number of output files given
        # the lower index has to be changed to be less then the upper index
        lower_index = lower_step_limit - start_step
        if lower_index < 0:
            raise ValueError(f"The given star_step {start_step} is higher then the lower limit in the pattern '{found.group()}' in line {i} of the template file.")
        
        # The dash and second number can be omitted:
        # e.g. <4> is equivalent to <4-4>
        if (not groups[1]) and (groups[2] is None):
            # To include anything the upper index has to be increased by 1
            step_limits = (lower_index, lower_index + 1)

        # If the second number is omitted but the dash is not, the upper limit is the last step: 
        # e.g. <4-> is equivalent to <4-10> if 10 output files are generated
        elif not groups[2]:
            # the number of files given is used for the upper index (it is already 1 greater then the highest possible index)
            upper_index = end_step
            step_limits = (lower_index, upper_index)

        # both numbers are present in the pattern
        else:
            upper_step_limit = int(groups[2])
            upper_index = upper_step_limit - start_step

            step_limits = (lower_index, upper_index)

        num_files_with_current_line = (step_limits[1] - step_limits[0])
        if num_files_with_current_line > end_step:
            raise ValueError(f"The number of given output files is {end_step},"
            f" but line {i} of the template file is expected to appear in {num_files_with_current_line} output files (pattern: {found.group()}).") 
        
        # remove the steprange pattern and spaces between line content and pattern 
        line_content = STEPRANGEREGEX.sub("", l).rstrip() 
        template_lines.append(Templateline(i, line_content, range(*step_limits), found.group()))

    return template_lines, removed_lines


def split_stepfile_lines(template_lines, output_filepaths, start_step):

    lines_per_stepfile = defaultdict(list)
    for line in template_lines:
        for step in line.outputfile_index_range:
            lines_per_stepfile[output_filepaths[step]].append(line)

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

    template_lines, removed_lines = parse_lines_and_stepranges(template_lines, args.start_step, len(output_filepaths)) 

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
