

dictionary = {}

x=input("Enter the your name:")
dictionary.update({"name":x})

y=int(input("Enter the your age:"))
dictionary.update({"age":y})

z=input("Enter the your course:")
dictionary.update({"dob":z})

for key, value in dictionary.items():
    print(key,":",value)

