from typing import TextIO
import argparse
import glob
import sys

def sys_write(message: str) -> None:
    """Shortens sys.stdout.write + newline"""
    sys.stdout.write(message + "\n")

def sys_error(message: str) -> None:
    """Shortens sys.stderr.write + newline"""
    sys.stderr.write(message + "\n")

def setup_argparse() -> None:
    """Sets up argparse arguments and variables"""
    global args
    parser = argparse.ArgumentParser()

    # positional argument
    parser.add_argument("pattern", help="the pattern we want to search for", nargs="?")
    parser.add_argument("file", help="the file to be searched", nargs="*")

    # optional arguments
    parser.add_argument("-n", "--number_output_lines", help="print line numbers alongside matches", action="store_true")
    parser.add_argument("-c", "--count_of_matches", help="print only the count of matching lines", action="store_true")
    parser.add_argument("-i", "--case_insensitive", help="case-insensitive matching", action="store_true")
    parser.add_argument("-v", "--invert_match", help="invert match, print lines that do NOT match", action="store_true")

    args = parser.parse_args()

def file_detected(file: TextIO) -> None:
    """When file is detected, open file and output matches"""
    count = 1
    
    for line in file:
        line = line.strip()
        pattern = args.pattern
        to_print = line
        
        if args.case_insensitive:
            pattern = args.pattern.lower()
            line = line.lower()
        
        if args.number_output_lines:
            to_print = f"{count} {line}"
        
        if not args.invert_match and pattern in line:
            if args.count_of_matches:
                count += 1
                continue
            else:
                sys_write(to_print)
                count += 1

    if args.count_of_matches:
        sys_write(str(count - 1))

def file_and_pattern_detected() -> None:
    """Looks for matches in file name"""
    for file in args.file:
        formatted = file.split(".")[0]
        found_matches = glob.glob(f"./sample_files/{formatted}.*")

        if not found_matches:
            sys_error(f"[ERROR DETECTED] file: \"{file}\" does not exist")
            continue

        for match in found_matches:
            with open(match, 'r', encoding="utf-8") as f:
                file_detected(f)

def file_not_detected() -> None:
    """When file is not detected, acquire from stdin"""
    sys_write("Acquiring from stdin . . .") 
    count = 1
    
    for line in sys.stdin:
        line = line.strip()
        pattern = args.pattern
        to_print = line
        
        if args.case_insensitive:
            pattern = args.pattern.lower()
            line = line.lower()
        
        if args.number_output_lines:
            to_print = f"{count} {line}"
        
        if not args.invert_match and pattern in line:
            if args.count_of_matches:
                count += 1
                continue
            else:
                sys_write(to_print)
                count += 1
    
    if args.count_of_matches:
        sys_write(str(count - 1))

def validate_pattern_file_existence() -> None:
    """Validate if pattern and file exists from user input"""
    if args.pattern and args.file:
        file_and_pattern_detected()
    else:
        if not args.pattern:
            sys_error("[ERROR DETECTED] No pattern inputted")
            return
        
        if not args.file:
            sys_error("[ERROR DETECTED] No file inputted")
            file_not_detected()
            
def grep() -> None:
    """The main grep function"""
    validate_pattern_file_existence()


def main() -> None:
    setup_argparse()
    grep()

if __name__ == "__main__":
    main()
