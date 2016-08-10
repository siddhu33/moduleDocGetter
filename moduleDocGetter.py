import numpy as np
import shutil
import sys
import os

class docWriter:
    def __init__(self,libname,docs):
        self.libname = libname
        self.docs = docs
    def methods(self):
        return self.docs.keys()
    def printIndex(self):
        ul = "<ul>\n{0}\n</ul>".format("\n".join(["<li><a href=\"{0}.html\">{0}</a></li>".format(k) for k in self.docs.keys()]))
        with open(self.libname + "/" + "index.html","w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>\n{0}</title>\n</head>\n<body>\n<h3>{0}</h3>\n<div>\n{1}\n</div>\n</body>\n".format(self.libname,ul))
    def export(self,mode):
        if mode == "text":
            for item in self.docs.items():
                with open(self.libname + "/" + item[0] + ".txt",'w') as f:
                    f.write(item[1])
        elif mode == "web":
            self.printIndex()
            for item in self.docs.items():
                with open(self.libname + "/" + item[0] + ".html","w") as f:
                    f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>\n{0}</title>\n</head>\n<body>\n<pre>\n{1}\n</pre>\n</body>\n".format(item[0],item[1]))
def main():
    if len(sys.argv) < 3:
        print "USAGE - python moduleDocGetter.py [module name] [export type]"
        return
    print "Module Document Getter"
    libname = sys.argv[1]
    exportType = sys.argv[2]
    print "export type : {0}".format(exportType) 
    if exportType != "web" and exportType != "text":
        raise ValueError("Export type is either 'web' or 'text'. Please insert one of the two.")
    print "Module to search for documents - {0}".format(libname)
    if not os.path.exists(libname):
        try:
            os.makedirs(libname)
        except OSError:
            pass
    parts = libname.split('.')
    lib = __import__(libname)
    if len(parts) > 1:
        for i in range(1,len(parts)):
            lib = lib.__dict__[parts[i]]
    d = dir(lib)
    ndocs = 0
    docs = {}
    for i in d:
        if('__doc__' in dir(lib.__dict__[i])):
            ndocs += 1
            docs[i] = str(lib.__dict__[i].__doc__)
    print "{0} function {1} obtained from module {2}".format(ndocs,"document" if ndocs == 1 else "documents",libname)
    writer = docWriter(libname,docs)
    writer.export(exportType)
main()
