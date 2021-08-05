#!/usr/bin/env python3

import math, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--action", dest="action", default="create", help="'create' for create new list | 'print' for print list")
parser.add_argument("--max", dest="max", default="100", help="Max value for 2D-List")
parser.add_argument("--length", dest="inn", default="5", help="Inner list length")
parser.add_argument("--append", dest="a", default="w", help="Append to new line\nDefault is 'w' | Write and overwrite data if data exists | 'a' for append")
parser.add_argument("--file", dest="file", default="list", help="File name for 2D-List")
args = parser.parse_args()


mx = int(args.max)
inn = int(args.inn)
file_name = args.file + '.txt'

def create_list():
    data = []
    data_inner = []
    count = 1
    vl = 1
    for _ in range(1, math.ceil(mx/inn)+1):
        for val in range(vl, mx+1):
            if count > inn:
                continue
            data_inner.append(val)
            count += 1
            vl = val + 1
        data.append(data_inner)
        data_inner = []
        count = 1
    try:
        with open(file_name, args.a) as file:
            file.write(f"{data}\n")
    except Exception as e:
        print("Error:", e)


def main():
    try:
        if args.action == "write":
            create_list()
        else:
            act = ""
            if args.action == "print":
                act = "r"
            elif args.action == "clear":
                act = "w"

            with open(file_name, act) as file:
                if act == "r":
                    print(file.read())
                elif act == "w":
                    file.write("")
    except Exception as e:
        print("Error:", e)


main()
