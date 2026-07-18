import argparse

def setup_argparse() -> None:
    """Set up argparse variables"""
    global args
    parser = argparse.ArgumentParser()
    
    # positional argument/s
     
     
    # optional argument/s

    args = parser.parse_args()

def main() -> None:
    setup_argparse()

if __name__ == '__main__':
    main()
