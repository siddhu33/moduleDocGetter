import numpy as np
import sys
import os

def to_file(name,s):
    with open(name + ".txt",'w') as f:
        f.write(str(s))

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
    docs = 0
    for i in d:
        if('func_doc' in dir(lib.__dict__[i])):
            docs += 1
            to_file(libname + "/" + i,lib.__dict__[i].func_doc)
    print "{0} function {1} obtained from module {2}".format(docs,"document" if docs == 1 else "documents",libname)
main()
