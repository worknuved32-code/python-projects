a=[]
n=int(input("Enter the n value:"))
for i in range(n):
    ele=int(input("Enter the  element:"))
    a.append(ele)
print("inserted list",a)
for i in a:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(f"factorail of {i} is {fact}")

