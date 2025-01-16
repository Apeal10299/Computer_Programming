#Using command-line arguments involves the sysmodule.
#Review the docs for this module and using the information in there write a short program that when run from the command-line reports what operating system platform is being used.

import sys

def main():
    platform = sys.platform
    print(f"You are running on: {platform}")
main()
