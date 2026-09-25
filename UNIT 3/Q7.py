import shutil
import os


with open("source.txt", "w") as file:
    file.write("This is a sample file.")


shutil.copy("source.txt", "copy.txt")
print("File copied successfully.")


shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")


os.remove("moved.txt")
print("File deleted successfully.")