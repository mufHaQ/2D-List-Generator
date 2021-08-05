#!/usr/bin/env python3

import math
import argparse
from os import access


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--max", dest="max", default="10", help="Max value for 2D-List\ndefault [10]")
parser.add_argument("--len", dest="inner", default="2", help="Inner list length\ndefault [2]")
parser.add_argument("--file", dest="file", default="list", help="File name for 2D-List")
parser.add_argument("--append", action="store_true", help="Append list to file")
parser.add_argument("--write", action="store_true", help="Write list")
parser.add_argument("--print", action="store_true", help="Print list from file to console")
parser.add_argument("--clear", action="store_true", help="Clear list from file")
args = parser.parse_args()


max = int(args.max)
length = int(args.inner)
file_name = args.file + '.txt'


def create_list():
    data = []
    count = 1
    append = ""
    for outer in range(1, math.ceil(max/length)+1):
        data.append([])
        for _ in range(1, length+1):
            if count > max:
                break
            data[outer-1].append(count)
            count += 1
    try:
        append = "w"
        if args.append:
            append = "a"
        with open(file_name, append) as file:
            file.write(f"{data}\n")
    except Exception as e:
        print("Error:", e)


def command_handler():
    if args.write:
        create_list()
    else:
        if args.print:
            with open(file_name) as file:
                print(file.read(), end="")
        elif args.clear:
            with open(file_name, 'w+') as file:
                file.write("")


def main():
    try:
        command_handler()
    except Exception as e:
        print("Error:", e)


main()
