import argparse
import sys
from typing import TextIO

def sys_write(message: str) -> None:
    """Shortens sys.stdout.write and flushes with a newline"""
    sys.stdout.write(message + "\n")

def sys_error(message: str) -> None:
    sys.stderr.write(message + "\n")

def file_only(f: TextIO) -> None:
    for line in f:
        line = line.strip()
        sys_write(line)

def number_output_lines(f: TextIO) -> None:
    count = 1
    for line in f:
        line = line.strip()
        sys_write(f"{count} {line}")
        count += 1

def number_non_blank_lines(f: TextIO) -> None:
    count = 1
    for line in f:
        line = line.strip()
        if line != "":
            sys_write(f"{count} {line}")
            count += 1
        else:
            sys_write(line)

def setup_parser() -> None:
    """Sets up argparse and the arguments"""
    global parser
    global args

    parser = argparse.ArgumentParser()
    
    parser.add_argument("file", help="file you wish to work with", nargs="*")
    parser.add_argument("-n", "--number_output_lines", help="number every output line", action="store_true")
    parser.add_argument("-b", "--number_non_blank_lines", help="number every non-blank lines", action="store_true")

    args = parser.parse_args()

def file_not_detected() -> None:
    """When file is not inputted, acquire datafrom stdin instead"""
    sys_write("file not detected") 
    sys_write("acquiring user input: \n") 
    
    for line in sys.stdin:
        user_input = line.strip()
        sys_write("inputted: " + user_input)

def file_detected() -> None:
    "File/s are detected, output the data to the terminal"
    sys_write("file/s detected" + "\n")
    
    for file in args.file:
        try:
            with open(f"./sample_files/{file}", 'r', encoding="utf-8") as f:
                if args.number_output_lines:
                    number_output_lines(f)
                        
                elif args.number_non_blank_lines:
                    number_non_blank_lines(f)
                
                else:
                    file_only()
                    
        except FileNotFoundError:
            sys_error(f"[ERROR DETECTED] File: {file} is not found")

def cat() -> None: # needs a better name for this
    if not args.file:
        file_not_detected()        
    else:
        file_detected()



def main() -> None:
    setup_parser()
    cat()    


if __name__ == "__main__":
    main()

    