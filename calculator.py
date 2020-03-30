#!/usr/bin/env python

def helloworld():
    print(f"Hello World ! this is my first pip package")
    
def sum(x):
    y = x+x
    return y

def sqr(x):
    return x * x

def cube(x):
    return x * x * x

def name(x):
    numNames = ["Zero", "One", "Two", "Three", "Four", "To be added"]
    if x< 5:
        name = numNames[x]
    else:
        name = numNames[5]
    return name
