from typing import TextIO
import argparse
import sys
import glob

def sys_write(message: str) -> None:
    """Shortens sys.stdout.write and flushes with a newline"""
    sys.stdout.write(message + "\n")

def sys_error(message: str) -> None:
    """Shortens sys.stderr.write and flushes with a newline"""
    sys.stderr.write(message + "\n")

def setup_parser() -> None:
    """Sets up argparse and the arguments"""
    global parser
    global args

    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="file you wish to work with", nargs="*")
    parser.add_argument("-n", "--number_output_lines", help="number every output line", action="store_true")
    parser.add_argument("-b", "--number_non_blank_lines", help="number every non-blank lines", action="store_true")

    args = parser.parse_args()

def output_content(file: TextIO) -> str | None:
    """Outputs content given file input"""
    count = 1

    for line in file:
        line = line.strip()

        if args.number_output_lines:
            sys_write(f"{count} {line}")
            count += 1

        elif args.number_non_blank_lines:
            if line == "":
                sys_write(f"{count} {line}")
                count += 1
            else:
                sys_write(line)

        else:
            sys_write(line)

def file_not_detected() -> None:
    """When file is not inputted, acquire data from stdin instead"""
    sys_write("file not detected")
    sys_write("acquiring user input: \n")

    for line in sys.stdin:
        user_input = line.strip()
        sys_write("inputted: " + user_input)

def file_detected() -> None:
    """If files are inputted, look for file matches in the sample_files/ folder"""
    global is_error 
    
    for file in args.file:
        formatted = file.split(".")[0]
        found_matches = glob.glob(f"./{formatted}.*")

        if not found_matches:
            sys_error(f"[ERROR DETECTED] File: '{file}' is not found" + "\n")
            is_error = True
            continue

        for match in found_matches:
            with open(match, 'r', encoding="utf-8") as f:
                output_content(f)

def cat() -> None:
    """Calls the appropriate functions to output content to the terminal"""
    if not args.file:
        file_not_detected()
    else:
        file_detected()


def main() -> None:
    global is_error
    is_error = False
    
    setup_parser()
    cat()
    sys.exit(is_error)


if __name__ == "__main__":
    main()

