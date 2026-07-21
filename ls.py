import argparse
import sys
from pathlib import Path

def sys_write(message: str):
    """Shortens sys.stdout.write() and automatically adds a newline"""
    sys.stdout.write(message + "\n")

def sys_error(message: str):
    """Shortens sys.stderr.write() and automatically adds a newline"""
    sys.stderr.write(message + "\n")

def setup_argparse() -> None:
    """Set up argparse variables"""
    global args
    parser = argparse.ArgumentParser()

    # positional argument/s
    parser.add_argument("directory", help="a directory to search", nargs="?")

    # optional argument/s
    parser.add_argument("-a", "--show_hidden_files", help="show hidden files (dotfiles)", action="store_true")
    parser.add_argument("-l", "--long_format", help="long format showing permissions, size, and modified date")
    parser.add_argument("-r", "--reverse_order", help="shows the directories in Z-A format", action="store_true")

    args = parser.parse_args()

def specified_dir() -> None:
    """Validates and searches the specified directory"""
    parent_dir = Path("./")
    sub_dir = parent_dir / args.directory

    if sub_dir.is_dir():
        sys_write(f'{sub_dir} exists\n')
        ordered_dir = sorted([item.name for item in sub_dir.iterdir()], key=str.lower)
        
        for item in ordered_dir:
            dotfile_check = item.split('.')[0] != ''
            if dotfile_check:
                sys_write(item)
        
    else:
        sys_error(f"Sub Directory: {sub_dir} does not exist")


def no_specified_dir() -> None:
    """Search the current directory"""
    directory = Path("./")
    my_dir = sorted([item.name for item in directory.iterdir()], key=str.lower)

    for item in my_dir:
        dotfile_check = item.split('.')[0] != ""

        if dotfile_check:
            sys_write(item)

def dir_existence_check() -> None:
    """Checks for the directory input"""
    if args.directory:
        specified_dir()
    else:
        no_specified_dir()

def ls() -> None:
    dir_existence_check()


def main() -> None:
    setup_argparse()
    ls()

if __name__ == '__main__':
    main()
