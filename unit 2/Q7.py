num = [1,2,3,4,5,56,65,43]

squ = [x * x for x in num]

print("squ",squ)

squ_dict = {x: x * x for x in num}

print("squ_dict",squ_dict)

squ_set = {x * x for x in num}

print("squ_set",squ_set)
