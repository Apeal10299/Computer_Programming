#Write a program that takes the name of a file as a command-line argument, and creates a backup copy of that file. 
# The backup should contain an exact copy of the contents of the original and should, obviously, have a different name.
# Hint: By now, you should be getting the idea that there is a built-in way to do the heavy li ing here! Take a look at the "Brief Tour of the Standard Library" in the docs.

import sys
import shutil

def main():
    if len(sys.argv) != 2:
        print("Usage: python Task6.py <file_name>")
        return

    original_file = sys.argv[1]
    try:
        backup_file = f"{original_file}_backup"

        shutil.copy(original_file, backup_file)
        print(f"Backup created successfully: {backup_file}")
    except FileNotFoundError:
        print(f"Error: The file '{original_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{original_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()

