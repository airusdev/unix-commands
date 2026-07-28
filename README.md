# GNU Commands Reimplementation

## What is this?

This project is a simple reimplementation of GNU commands, mainly **cat**, **wc**, and **grep**, using Python.

**ls** and **find** were also added in the original project tree. However, these three commands proved to be enough to learn the concepts I needed.

## Why did I build this?

This project was built to help me understand thinking in streams—how information is processed when bit by bit of information flows.

Instead of having to process information in one big batch with `file.read()`, which requires tons of effort to clean and process, we use `for line in file` to instead process the information line by line. This makes the information easier to clean and process.

If we were to read a file that's 10GB in one go, with system limitations, our program is bound to create a bottleneck, possibly even causing the program not to work. If we streamed it line by line, it makes sure that no matter how large the file given to us, it can be safely, quickly, and easily processed.

## Why only cat, grep, and wc?

I decided that **cat**, **grep**, and **wc** were enough because by then, I'd already understood the concept of streams.

If I were to continue with **ls** and **find**, it would be redundant because the files are just asking me to find and list files or directories.

## Code Structure

Each command is set up with a `main()` function, ensuring only one file runs at a time.

This is followed by single-responsibility functions such as:

* `setup_argparse`
* Shortening `sys.stdout.write()`
* Shortening `sys.stderr.write()`
* Checking for the existence of a file
* A function for when a file exists
* A function for when a file does not exist

The overall structure of the code starts from the very bottom and works to the very top, with `sys_error`, `sys_write`, and `setup_argparse` at the very top.

## Program Flow

The program starts in `main()`.

It first validates whether the file input exists.

If the file does not exist, it acquires input from `stdin`.

If the file exists, it calls the function for checking file matches. Our file matching function works even if you do not put an extension in the filename.

Afterwards, depending on the program, it processes the lines of the file according to its rules and expected output.
