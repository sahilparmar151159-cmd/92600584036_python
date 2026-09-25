import re

text = "Python is easy. Python is powerful. Python is popular."

result1 = re.match("Python", text)

if result1:
    print("match():", result1.group())

result2 = re.search("powerful", text)

if result2:
    print("search():", result2.group())

result3 = re.findall("Python", text)

print("findall():", result3)