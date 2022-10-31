# !/usr/bin/env python
# -*- coding :latin1 -*-
import math
a = input('Digite um valor a: ')
b = input('Digite um valor b: ')
c = input('Digite um valor c: ')

abc = [a, b, c]
s = (a+b+c)/2

maior = (max(int(number) for number in abc))

if maior == a:
    if a > b + c:
        print a, b, c
    else:
        area = s*((s-a)*(s-b)*(s-c))
        area = math.sqrt(area)
        print area

if maior == b:
    if b > a + c:
        print a, b, c
    else:
        area = s*((s-a)*(s-b)*(s-c))
        area = math.sqrt(area)
        print area

if maior == c:
    if c > a + b:
        print a, b, c
    else:
        area = s*((s-a)*(s-b)*(s-c))
        area = math.sqrt(area)
        print area

