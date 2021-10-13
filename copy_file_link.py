import sys
import os
import re


def clipboard(text):
    """Copies input 'text' to the command line. This string is evaluated twice so any special characters
     need to be escaped twice.
     """
    print(str(text))
    cmd = 'echo | set /p nul=' + str(text) + '| clip'
    os.system(cmd)


if len(sys.argv) == 3:
    full_path = sys.argv[1]
    full_path = full_path.replace('/', '\\')
    command = sys.argv[2]
    match = re.search(r"C:\\Users\\[A-Za-z ]+\\Dropbox \(Springboard\)\\", full_path)
    if match is None:
        print("Error: That does not look to be a file on dropbox")
        input()
    else:
        if command in "Full" or command in "Dir_Full":
            full_path = full_path.replace(match.group(0), "C:\\Users\\^^^%username^^^%\\Dropbox (Springboard)\\")
        elif command in "Partial" or command in "Dir_Partial":
            full_path = full_path.replace(match.group(0), "Dropbox (Springboard)\\")
        else:
            print("Error: Command not supported")
            input()
            exit()
        clipboard(full_path)
        print("Copied to clipboard")
        input()  # <- comment out this line to prevent the terminal opening

else:
    print("Error: Incorrect number of arguments passed in")
    input()
