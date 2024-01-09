#written by Pardesicat

import os
import sys
import platform
import time

def user_name ():

    name = input("Enter your name:")
    print (f"Namaste : {name}")


def system_det ():

    system = platform.system()

    if system == "Windows":
        print(f"You are using Windows.")
    elif system == "Linux":
        print(f"You are using Linux.")
    elif system == "Darwin":
        print(f"You are using macOS.")
    else:
        print(f"Sorry cant detect your system.")


def check_arch ():
    import platform
    platform = platform.architecture()
    print (f"Your Using {platform} Architect of Cpu" )


if __name__ == "__main__":
    
    user_name()
    time.sleep(3)

    system_det()
    time.sleep(4)

    check_arch()
    time.sleep(3)

    sys.exit()
