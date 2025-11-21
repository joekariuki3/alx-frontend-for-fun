#!/usr/bin/python

"""
Script that takes two arguments, markdown_file_name, output_file_name
"""

if __name__ == "__main__":
    import os
    import sys

    argc = len(sys.argv)
    if argc < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html \n")
        exit(1)
    elif argc >= 2:
        markdown_file_name = sys.argv[1]

        if not os.path.exists(markdown_file_name):
            sys.stderr.write(f"Missing {markdown_file_name}\n")
            exit(1)
