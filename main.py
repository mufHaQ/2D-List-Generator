#!/usr/bin/env python3

import math, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--action", dest="action", default="create", help="'create' for create new list | 'print' for print list")
parser.add_argument("--max", dest="max", default="100", help="Max value for 2D-List")
parser.add_argument("--length", dest="inner", default="5", help="Inner list length")
parser.add_argument("--append", dest="append", default="w", help="Append to new line\nDefault is 'w' | Write and overwrite data if data exists | 'a' for append")
parser.add_argument("--file", dest="file", default="list", help="File name for 2D-List")
args = parser.parse_args()


max = int(args.max)
length = int(args.inner)
file_name = args.file + '.txt'
action = args.action


def create_list():
    data = []
    count = 1

    for outer in range(1, math.ceil(max/length)+1):
        data.append([])
        for _ in range(1, length+1):
            data[outer-1].append(count)
            count += 1
    try:
        with open(file_name, args.append) as file:
            file.write(f"{data}\n")
    except Exception as e:
        print("Error:", e)


def command_handler():
    if action == "write":
        create_list()
    else:
        act = ""
        if action == "print":
            act = "r"
        elif action == "clear":
            act = "w"
        with open(file_name, act) as file:
            if act == "r":
                print(file.read())
            elif act == "w":
                file.write("")


def main():
    try:
        command_handler()
    except Exception as e:
        print("Error:", e)


main()
