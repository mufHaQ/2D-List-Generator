#!/usr/bin/env python3

import math, argparse
from typing import Reversible

parser = argparse.ArgumentParser()
parser.add_argument("--action", dest="action", default="create", help="'create' for create new list | 'print' for print list")
parser.add_argument("--max", dest="max", default="100", help="Max value for 2D-List")
parser.add_argument("--length", dest="inn", default="5", help="List length")
parser.add_argument("--append", dest="a", default="w", help="Append to new line\nDefault is 'w' | Write and overwrite data if data exists | 'a' for append")
parser.add_argument("--file", dest="file", default="list", help="File name for 2D-List")
args = parser.parse_args()



def create_list():
    mx = int(args.max)
    inn = int(args.inn)
    data = []
    data_inner = []
    count = 1
    vl = 1
    file_name = args.file + '.txt'
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

if args.action == "create":
    create_list()
elif args.action == "print":
    with open('list.txt') as file:
        print(file.read())
