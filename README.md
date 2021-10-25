Springboard Tools

These tools add options to your right click context menu to:
- Copy full dropbox path (adjusted to work for any user by replacing your username with %username%)
- Copy partial dropbox path (just the Dropbox folder structure)
- Draft upissue of file (create copy with new filename)
- Release upissue of file (rename to remove draft version number)

Installation:
- Install Python3 on your computer
- Copy this folder (i.e. SpringboardTools) onto your machine.
- Run generate_registry_file.py (See 1. for help)
- Double click springboard_tools.reg and add the file to your computer's registry. (See 2. for help)
- The tools should now be installed on you computer.

Once installed, right click on a dropbox file and you should see a "Springboard" sub menu, with the various tool options in there.

The keys added in the registry run the .py scripts in your SpringboardTools folder with the selected file\folder path 
as an argument. If you want to edit or add to the functionality of the tools you can simply edit those python scripts.


Uninstallation:
- Double click "Uninstall_springboard_tools.reg". This will remove the Springboard sub menu from your right click.
- Delete your copy of the Springboard Tools folder.



Help:
1. (The .py file may automatically be run by python, or it might open with your chosen IDE. 
  In the latter case you can run the script from your IDE. If the file opens in a simple text editor such as notepad, 
  you will have to select 'open with' and then pick python. If python is not an option you will have to find the 
  location of your python.exe executable.) This should generate a .reg registry file called "springboard_tools.reg"
2. (This adds the Springboard sub menu to your right click menu. You will have click yes to allow the registry editor to 
  make changes to your computer and click yes to the following warning asking if you want to continue. A pop-up should
  inform you that the keys have been successfully added to  the registry)