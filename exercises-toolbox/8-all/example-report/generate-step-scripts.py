import re
import sys
from collections import defaultdict

STEPRANGEREGEX = re.compile(r"(?:#|%)\s<(\d*)(-(\d*)|)>")



def extract_stepranges(lines):
    step_ranges = []
    script_lines = []
    for i,l in enumerate(lines):
        found = STEPRANGEREGEX.search(l)
        if found is None: 
            continue
        groups = found.groups()

        lower_limit = int(groups[0])
        if (not groups[1]) and (groups[2] is None):
             step_range = (lower_limit, lower_limit)
        elif not groups[2]:
            step_range = (lower_limit, None)
        else:
            step_range = (lower_limit, int(groups[2]))
        step_ranges.append(step_range)
        script_lines.append(STEPRANGEREGEX.sub("", l).rstrip())

    return step_ranges, script_lines


def step_list_from_step_range(step_range, upper_limit):
    lower_limit = int(step_range[0])
    if not step_range[1] is None:
        upper_limit = int(step_range[1])
    return list(range(lower_limit, upper_limit+1))



def generate_step_file_lines(template_lines):
    step_ranges, script_lines = extract_stepranges(template_lines)
    highest_upper_limit = max([int(sr[1]) for sr in step_ranges if sr[1]]) + 1

    step_lists = [step_list_from_step_range(sr, highest_upper_limit) for sr in step_ranges]
     
    files_lines = defaultdict(list)
    for sl, line in zip(step_lists, script_lines):
        print(f"sl: {sl}: {line}")
        for step in sl:
            files_lines[step].append(line)
    

    return files_lines


def main():
    filepath = sys.argv[1]
    print(f"Filename: {filepath}")
    output_filepath = filepath 
    if len(sys.argv) > 2:
        output_filepath = sys.argv[2]

    path, ext = output_filepath.rsplit('.') 
    output_filepath_pattern =  path + "_step-{step}." + ext
    print(output_filepath, output_filepath_pattern)
    with open(sys.argv[1]) as fh:
        script_lines = fh.readlines()
    
    files_lines = generate_step_file_lines(script_lines)

    for it in files_lines.items():
        print(it)
    
    for step, lines in files_lines.items():
        with open(output_filepath_pattern.format(step=step), "w") as fh:
            fh.write("\n".join(lines).strip())
        

if __name__ == "__main__":
    main()
