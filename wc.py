from typing import TextIO
import argparse
import sys
import glob

def sys_write(message: str) -> None:
    """Shortens sys.stdout and adds a newline"""
    sys.stdout.write(message + "\n")

def sys_error(message: str) -> None:
    """Shortens sys.stderr and adds a newline"""
    sys.stderr.write(message + "\n")

def setup_argparse() -> None:
    """Setups argparse arguments"""
    global args
    parser = argparse.ArgumentParser()

    # positional arguments
    parser.add_argument("file", help="the file to search on", nargs="*")

    # optional arguments
    parser.add_argument("-l", "--lines_only", help="only output number of lines", action="store_true")
    parser.add_argument("-w", "--words_only", help="only output number of words", action="store_true")
    parser.add_argument("-c", "--bytes_only", help="only output number of bytes", action="store_true")

    args = parser.parse_args()

def setup_variables() -> None:
    """Setups the lines, word, byte variables for output"""
    global lines
    global words
    global bytes_

    lines = 0
    words = 0
    bytes_ = 0

def output_results() -> None:
    sys_write(f"{lines} {words} {bytes_}") 

def count_words(line: str) -> int:
    line = line.strip().split(" ")
    word_count = len(line)
    
    return word_count

def count_bytes(line: str) -> int:
    line = line.encode("utf-8")
    bytes_count = len(line)

    return bytes_count

def count_occurrences_in_file(file: TextIO) -> None:   
    """Acquires the total number of occurrences of lines, word, and bytes"""
    global lines
    global words
    global bytes_ 
    
    for line in file:
        line = line.strip()

        lines += 1
        words += count_words(line)
        bytes_ += count_bytes(line)

    output_results()

def look_for_file_matches() -> None:
    """Looks for file matches in the files directory"""
    for file in args.file:
        formatted = file.split(".")[0]
        found_matches = glob.glob(f"./sample_files/{formatted}.*")

        if not found_matches:
            sys_error(f"[NO FILE FOUND] File: {file}")
            continue

        for match in found_matches:
            with open(match, 'r', encoding="utf-8") as f:
                count_occurrences_in_file(f)

def file_not_exists() -> None:
    """If file does not exist, acquire from stdin"""
    sys_write("[NO FILE DETECTED] Acquiring from stdin . . .")

    for line in sys.stdin:
        line = line.strip()
        sys_write(line)
        # code here


def file_existence() -> None:
    """Validates if file from input exists"""
    if args.file:
        look_for_file_matches()
    else:
        file_not_exists()

    return


def wc() -> None:
    file_existence()


def main() -> None:
    setup_argparse()
    setup_variables()
    wc()

if __name__ == '__main__':
    main()