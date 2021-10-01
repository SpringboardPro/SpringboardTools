import sys;
import os;
import re;
import shutil;

def clipboard(text):
    print(str(text))
    cmd = 'echo | set /p nul=' + str(text) + '| clip'
    os.system(cmd)

if len(sys.argv) == 3 :
    fullpath = sys.argv[1]
    command = sys.argv[2]
#    print(fullpath)
#    print(command)
    match = re.search(r'C:\\Users\\[A-Za-z ]+\\Dropbox \(Springboard\)\\', fullpath)
#    print(match.group(0))
    if (match == None) :
        print("Error: That does not look to be a file on dropbox")
        input()
    else :
#    print (match)
        if command in "Full" : 
            fullpath = fullpath.replace(match.group(0),"C:\\Users\\^^%username^^%\\Dropbox (Springboard)\\")
        elif command in "Partial" :
            fullpath = fullpath.replace(match.group(0),"Dropbox (Springboard)\\")
        else :
            print("Error: Command not supported")
            intput()
            exit()
        clipboard(fullpath)
        print("Copied to clipboard")
        input() # <- comment out this line to prevent the terminal opening
    
else :
    print("Error: Incorrect number of arguements passed in")
    input()
