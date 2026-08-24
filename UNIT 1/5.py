list = [10,30,20,40,60,50,70,90]

print("enter the first element",list[0])
print("enter the third element",list[2])
print("enter the last element",list[-1])

list.append(90)
print("appended",list)

list.insert(1,50)
print("after inserted",list)

list.remove(20)
print("after removing",list)

squere = [x**2 for x in list]
print(squere)

even_numbers = [x for x in list if x % 2 == 0]
print("Even numbers:", even_numbers)
