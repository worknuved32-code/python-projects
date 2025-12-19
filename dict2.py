dict={}

n=int(input("Enter how many contacts?"))

for i in range(n):
    name=input("Enter  name:")
    phone=input("Enter  phone number:")
    if len(phone)<10 or len(phone)>10:
        print("Invalid phone number .\n "
        "try again")
        exit()
    dict[name]=phone

search=input("Enter the name to search:")    
if search in dict: 
    print("Phone number :",dict[search])
else:
    print("contact not found")
          