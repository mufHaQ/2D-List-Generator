#!/usr/bin/env python3

import math

def create_list(mx, gp):
    data = []
    data_inner = []
    count = 1
    vl = 1

    for _ in range(1, math.ceil(mx/gp)+1):
        
        for val in range(vl, mx+1):

            if count > gp:
                continue

            data_inner.append(val)
            count += 1
            vl = val + 1
            
        data.append(data_inner)
        data_inner = []
        count = 1
        
    return data

data = create_list(100, 10)

print(data)
print(len(data))
