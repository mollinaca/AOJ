#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        exit ()
    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                print ("#",end="")
        else:
            for j in range(w):
                if j == 0 or j == w-1:
                    print ("#",end="")
                else:
                    print (".",end="")
        print ()
    print ()