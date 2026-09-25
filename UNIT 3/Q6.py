import os
import sys


print("Current Directory:", os.getcwd())


folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created.")
else:
    print("Directory already exists.")


print("Directory contents:")
print(os.listdir())


print("Python Version:", sys.version)

print("Command-line arguments:", sys.argv)