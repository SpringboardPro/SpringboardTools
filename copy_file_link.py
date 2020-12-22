import sys;
import os;
import re;
import shutil;

from tkinter import Tk

if len(sys.argv) == 3 :
    fullpath = sys.argv[1]
    command = sys.argv[2]
    print(fullpath)
    match = re.search(r'C:\\Users\\[A-Za-z ]+\\Dropbox \(Springboard\)\\', fullpath)
#    print(match)
    if (match == None) :
        print("Error: That does not look to be a file on dropbox")
        input()
    else :
#    print (match)
        if command in "Full" : 
            fullpath = fullpath.replace(match.group(0),"C:\\Users\\%username%\\Dropbox (Springboard)\\")
        else :
            fullpath = fullpath.replace(match.group(0),"Dropbox (Springboard)\\")
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
