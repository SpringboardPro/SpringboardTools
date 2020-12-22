import sys;
import os;
import re;
import shutil;

if len(sys.argv) == 3 :
    split_path = os.path.split(sys.argv[1])
    upissue = sys.argv[2]
    old_file = split_path[1]
    print("Old Filename: " + old_file)
    path = split_path[0]
    old_file_parts = re.split(r'([A-Z]{3})-([0-9]{5})-rev([A-Z])([0-9]*) ',old_file)

    if old_file_parts[4] == '' :
        old_file_parts[4] = '0'
    
    if len(old_file_parts) == 6 :
        if upissue in "Draft" :
            print ("Draft Version upissue")
            if (old_file_parts[4] == '0') :
                if (old_file_parts[3] == 'Z') :
                    print("Error: Existing version is at Z. Sorry but I've not been told where we go after Z!")
                    input()
                    exit()
                major_version = chr(ord(old_file_parts[3])+1)
                minor_version = 1
            else :
                major_version = old_file_parts[3]
                minor_version = int(old_file_parts[4])+1
            new_file = "%s-%s-rev%s%d %s" % (old_file_parts[1],old_file_parts[2],major_version,minor_version,old_file_parts[5])
            print("New Filename: " + new_file)
            if os.path.isfile(path + "/" + new_file) == 0 :
                shutil.copy(path + "/" + old_file, path + "/" + new_file)
                print("File copied OK")
            else :
                print("Error: New file already exists")
        elif upissue in "Release" :
            print ("Release Version upissue")
            if (old_file_parts[4] == '0') :
                print("Error: This is already a released document")
                input()
                exit()
            new_file = "%s-%s-rev%s %s" % (old_file_parts[1],old_file_parts[2],old_file_parts[3],old_file_parts[5])
            print("New Filename: " + new_file)
            if os.path.isfile(path + "/" + new_file) == 0 :
                os.rename(path + "/" + old_file, path + "/" + new_file)
                print("File renamed OK")
            else :
                print("Error: New file already exists")
        else :
            print ("Error: Upissue method undefined")
            input()
            exit()
    else :
        print("Error: Filename was not as expected")

else :
    print("Error: Incorrect number of arguements passed in")

input()
