import sys;
import os;
import re;
import shutil;

from tkinter import Tk

if len(sys.argv) == 2 :
    fullpath = sys.argv[1]
    print(fullpath)
    match = re.search(r'\\Users\\[A-Za-z ]+\\Dropbox \(Springboard\)\\', fullpath)
#    print(match)
    if (match == None) :
        print("Error: That does not look to be a file on dropbox")
        input()
    else :
#    print (match)
        fullpath = fullpath.replace(match.group(0),"\\Users\\%username%\\Dropbox (Springboard)\\")
        print (fullpath)
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(fullpath)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
    
else :
    print("Error: Incorrect number of arguements passed in")
    input()
