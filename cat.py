import argparse
import sys

# VALIDATORS
def validate_if_string(message: str) -> str:
    return None

def no_input() -> None:


def sys_write(message: str) -> str:
    """Shortens sys.stdout.write"""
    sys.stdout.write(message)

def setup_parser() -> None:
    """Sets up argparse and the arguments"""
    global parser
    global args

    parser = argparse.ArgumentParser()
    
    parser.add_argument("file", help="file you wish to work with", nargs="*")
    parser.add_argument("-n", "--number_output_lines", help="number every output line", action="store_true")
    parser.add_argument("-b", "--number_non_blank_lines", help="number every non-blank lines", action="store_true")

    args = parser.parse_args()

def detect_cat() -> None: # needs a better name for this
    if not args.file:
        sys_write("no files detected")
    else:
        sys_write("files detected")


def main() -> None:
    setup_parser()
    detect_cat()    


if __name__ == "__main__":
    main()

