from typing import TextIO
import argparse
import glob
import sys

def sys_write(message: str) -> None:
    sys.stdin.write(message + "\n")

def sys_error(message: str) -> None:
    sys.stderr.write(message + "\n")
    
def setup_argparse() -> None:
    global args
    parser = argparse.ArgumentParser()
    
    # positional argument
    parser.add_argument("file", help="the file which the file is going to search on", nargs="*")
    parser.add_argument("pattern", help="the pattern we want to look for on the file", nargs="*")

    # optional arguments
    parser.add_argument("-n", "--number_output_lines", help="print line numbers alongside matches", action="store_true") 
    parser.add_argument("-c", "--count_of_matches", help="print only the count of matching lines", action="store_true")
    parser.add_argument("-i", "--case_insenstive", help="case-insensitive matching", action="store_true")
    parser.add_argument("-v", "--invert_match", help="invert match, print lines that do NOT match", action="store_true")

    args = parser.parse_args() 

def file_pattern_detected() -> None:
    for file in args.file:
        for pattern in args.pattern:
            for line in file:
                line = line.strip()
                if pattern in line:
                    print("oh yeah")

def validate_pattern_file_existence() -> None:
    if args.pattern and args.file:
        file_pattern_detected()
    else:
        if not args.pattern:
            sys_error("[ERROR DETECTED] No pattern inputted")    
        if not args.file:
            sys_error("[ERROR DETECTED] No file inputted")

def grep() -> None:
    validate_pattern_file_existence()

def main() -> None:
    setup_argparse()
    grep()

if __name__ == "__main__":
    main()
