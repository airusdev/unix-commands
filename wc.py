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
    """Sets up the variables for the total occurrences of files"""
    global lines
    global words
    global bytes_

    lines = 0
    words = 0
    bytes_ = 0

def setup_total() -> None:
    """Sets up the variables for the total occurrences from each files"""
    global total_lines
    global total_words
    global total_bytes_

    total_lines = 0
    total_words = 0
    total_bytes_ = 0

def output_total() -> str: # what if it only does
    """Outputs the total lines, words, and bytes of all the files searched"""
    global total_lines
    global total_words
    global total_bytes_

    to_output = []
    default = f"{total_lines} {total_words} {total_bytes_}"

    if args.lines_only:
        to_output.append(total_lines)
    if args.words_only:
        to_output.append(total_words)
    if args.bytes_only:
        to_output.append(total_bytes_)

    if not to_output:
        to_output = default

    to_output = "".join(map(str, to_output))
    to_output += f" total"
    sys_write(to_output)

def output_results(file: TextIO, is_total: bool) -> None:
    """Outputs the total lines, words, and bytes of a file"""
    global lines
    global words
    global bytes_

    to_output = []
    default = f"{lines} {words} {bytes_}"

    if args.lines_only:
        to_output.append(lines)
    if args.words_only:
        to_output.append(words)
    if args.bytes_only:
        to_output.append(bytes_)

    if not to_output:
        to_output = default

    to_output = "".join(map(str, to_output))
    to_output += f" {file.name.split("/")[-1]}"

    sys_write(to_output)

def count_line(line: str) -> int:
    if "\n" in line:
        return 1

    return 0

def count_words(line: str) -> int:
    line = line.strip().split(" ")
    word_count = len(line)

    if line[0] == '':
        return 0

    return word_count

def count_bytes(line: str) -> int:
    line = line.encode("utf-8")
    bytes_count = len(line)

    return bytes_count

def count_occurrences_in_file(file: TextIO) -> None:
    """Acquires the total number of occurrences of lines, word, and bytes"""
    if len(args.file) > 1:
        global total_lines
        global total_words
        global total_bytes_

    global lines
    global words
    global bytes_

    for line in file:
        lines += count_line(line)
        words += count_words(line)
        bytes_ += count_bytes(line)

        if len(args.file) > 1:
            total_lines += lines
            total_words += words
            total_bytes_ += bytes_

    output_results(file)

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

    if len(args.file) > 1:
        output_total()

def file_not_exists() -> None:
    """If file does not exist, acquire from stdin"""
    global lines
    global words
    global bytes_

    sys_write("[NO FILE DETECTED] Acquiring from stdin . . .")

    for line in sys.stdin:
        lines += count_line(line)
        words += count_words(line)
        bytes_ += count_bytes(line)

        sys_write(f"{lines} {words} {bytes_}")

def check_file_existence() -> None:
    """Validates if file from input exists"""
    if args.file:
        if len(args.file) > 1:
            setup_total()
        look_for_file_matches()
    else:
        file_not_exists()

    return

def wc() -> None:
    check_file_existence()


def main() -> None:
    setup_argparse()
    setup_variables()
    wc()

if __name__ == '__main__':
    main()