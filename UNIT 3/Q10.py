import re

with open("data.txt", "r") as file:
    text = file.read()

names = re.findall(r"Name:\s*(\w+)", text)

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

phones = re.findall(r"\b\d{10}\b", text)

print("Names:", names)
print("Emails:", emails)
print("Phone Numbers:", phones)