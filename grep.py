import argparse

def setup_argparse() -> None:
    parser = argparse.ArgumentParser()
    
    # positional argument
    parser.add_argument("file", help="file the system is going to search on", nargs="*")

    # optional arguments
    parser.add_argument("-n", "--number_output_lines", help="print line numbers alongside matches", action="store_true") 
    parser.add_argument("-c", "--count_of_matches", help="print only the count of matching lines", action="store_true")
    parser.add_argument("-i", "--case_insenstive", help="case-insensitive matching", action="store_true")
    parser.add_argument("-v", "--invert_match", help="invert match, print lines that do NOT match", action="store_true")

    args = parser.parse_args() 

def main() -> None:
    setup_argparse()

if __name__ == "__main__":
    main()
