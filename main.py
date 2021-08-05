#!/usr/bin/env python3

import math, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--action", dest="action", default="write", help="'create' for create new list | 'print' for print list")
parser.add_argument("--max", dest="max", default="10", help="Max value for 2D-List")
parser.add_argument("--len", dest="inner", default="2", help="Inner list length")
parser.add_argument("--append", dest="append", default="n", help="Append to new [y/n]")
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
            if count > max:
                break
            data[outer-1].append(count)
            count += 1
    try:
        append = "w"
        if args.append == "y":
            append = "a"
        
        with open(file_name, append) as file:
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
