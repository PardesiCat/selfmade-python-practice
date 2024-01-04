#written by Pardesicat

import os
import sys
import platform
import time

name = input("Enter your name:")
print (f"Namaste : {name}")

time.sleep(3)

system = platform.system()


if system == "Windows":
    print(f"{name} You are using Windows.")
elif system == "Linux":
    print(f"{name} You are using Linux.")
elif system == "Darwin":
    print(f"{name} You are using macOS.")
else:
    print(f"Sorry cant detect your system.")

time.sleep(2)



platform = platform.architecture()

print (f"{name} Your Using {platform} Architect of Cpu" )

time.sleep(3)

sys.exit()
