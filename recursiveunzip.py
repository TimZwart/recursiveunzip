#!/bin/python
import os;
import subprocess;

print 'unzipping all .src.zip files'

for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if filename.endswith(".src.zip"):
            filename_minuszip = filename[:-4]
            if not os.path.isfile(filename_minuszip):
                fullpath = "/".join([os.getcwd(), dirpath, filename])
                fullpath_minuszip = fullpath[:-4]
                com = 'unzip '+fullpath+' -d '+fullpath_minuszip
                print "command, $", com
                com2 = 'pwd'
                print "working dir according to subprocess, pwd"
                subprocess.call(com2, cwd=dirpath)
                print "file call"
                com3 = 'file '+fullpath
                print com3
                subprocess.call(com3, shell=True)
                subprocess.call(com, shell=True)
