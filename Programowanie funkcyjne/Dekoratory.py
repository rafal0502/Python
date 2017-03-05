#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Dekoratory modyfikują funkcje używając innych funkcji.
#Idealne,gdy chcemy rozszerzyć działanie funkcji bez modyfikowania jej

def decor(func):
    def wrap():
        print("========")
        func()
        print("========")
    return wrap


def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()


#Inny sposob wywolania
@decor
def print_text():
    print("Hello world!")

print_text()
