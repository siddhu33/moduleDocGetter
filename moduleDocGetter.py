import numpy as np
import sys
import os

def to_file(name,s):
    try:
        f = file(name + ".txt",'w')
        f.write(s)
        f.close()
    except:
        pass

def main():
    if len(sys.argv) < 2:
        raise ValueError("Needs library name")
    print "Module Document Getter"
    libname = sys.argv[1]
    print "Module to search for documents - {0}".format(libname)
    parts = libname.split('.')
    lib = __import__(libname)
    if len(parts) > 1:
        for i in range(1,len(parts)):
            lib = lib.__dict__[parts[i]]
    os.makedirs(libname)
    d = dir(lib)
    for i in d:
        if('func_doc' in dir(lib.__dict__[i])):
            to_file(libname + "/" + i,lib.__dict__[i].func_doc)

main()
