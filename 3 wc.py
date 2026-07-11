import argparse

def sys_write(message: str) -> None:
    """Shortens sys.stdout and adds a newline"""
    sys.stdout.write(message + "\n")

def sys_error(message: str) -> None:
    """Shortens sys.stderr and adds a newline"""
    sys.stderr.write(message + "\n")

def setup_argparse -> None:
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
    global word
    global byte
    
    lines = 0
    word = 0
    byte = 0

def output_results() -> None:
    return

def count_in_file() -> None:
    """Acquires the total number of occurrences of lines, word, and bytes"""
    return

def look_for_file_matches() -> None:
    """Looks for file matches in the files directory"""
    return

def file_exists() -> None:
    """If file exists, do the operation on the file"""
    return

def file_not_exists() -> None:
    """If file does not exist, acquire from stdin"""
    return

def file_existence() -> None:
    """Validates if file from input exists"""
    return


def wc() -> None:
    file_existence()


def main() -> None:
    setup_argparse()
    setup_variables()
    wc()

if __name__ == '__main__':
    main()