import os

def duplicate_finder(topdir=None):
    if topdir is None:
        topdir = os.getcwd()    #current working directory

    for root, dirs, files in os.walk(topdir):
        print(root, dirs, files)


duplicate_finder()
