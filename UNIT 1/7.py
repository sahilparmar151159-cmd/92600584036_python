student = {
    "name": "sahil",
    "age": 22,
    "marks": 69
}

print(student)

print("Name:", student["name"])
print("Keys:", student.keys())
print("Values:", student.values())


student["city"] = "Rajkot"

print("Updated dictionary:", student)


for key in student:
    print(key, ":", student[key])
