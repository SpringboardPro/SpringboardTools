import sys
import os

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

python_path = sys.executable
script_dir = os.path.abspath(os.path.dirname(__file__))

print(python_path)

# Writes a .reg file
f = open("springboard_tools.reg", "w")
f.write(r'Windows Registry Editor Version 5.00')
f.write('\n\n')
# Adds keys for files
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Copy Link - Full]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Copy Link - Full\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\copy_file_link.py\" \"%s\" Full"' % (
    python_path.replace("\\", "\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Copy Link - Partial]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Copy Link - Partial\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\copy_file_link.py\" \"%s\" Partial"' % (
    python_path.replace("\\", "\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Upissue - Draft]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Upissue - Draft\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\upissue.py\" \"%s\" Draft"' % (
    python_path.replace("\\", "\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Upissue - Release]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\springboard_sub_menu\springboard\Shell\Upissue - Release\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\upissue.py\" \"%s\" Release"' % (
    python_path.replace("\\", "\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\shell\springboard_anchor]')
f.write('\n')
f.write(r'"MUIVerb"="Springboard"')
f.write('\n')
f.write(r'"ExtendedSubCommandsKey"="*\\\\springboard_sub_menu\\\\springboard"')
f.write('\n')
f.write(r'"Icon"="%s\\SpringboardLogo.ico"' % (script_dir.replace("\\", "\\\\")))
f.write('\n\n')

# Adds keys for directory menu
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu\springboard]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu\springboard\Shell]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu\springboard\Shell\Copy Link - Full]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu\springboard\Shell\Copy Link - Full\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\copy_file_link.py\" \"%s\" Dir_Full"' % (
    python_path.replace("\\", "\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu\springboard\Shell\Copy Link - Partial]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\springboard_dir_sub_menu\springboard\Shell\Copy Link - Partial\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\copy_file_link.py\" \"%s\" Dir_Partial"' % (
    python_path.replace("\\", "\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\Directory\shell\springboard_dir_anchor]')
f.write('\n')
f.write(r'"MUIVerb"="Springboard"')
f.write('\n')
f.write(r'"ExtendedSubCommandsKey"="Directory\\\\springboard_dir_sub_menu\\\\springboard"')
f.write('\n')
f.write(r'"Icon"="%s\\SpringboardLogo.ico"' % (script_dir.replace("\\", "\\\\")))

f.close()

input()
