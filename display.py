<<<<<<< HEAD
print("id               product name            price")
print("101                   lays                 20")
print("102                  kurkere               40")
print("103                  biscuit                50")
print("104                   cake                  70")

amt=0
amt1=0
amt2=0
amt3=0



n=int(input("Enter the number of products :"))
for i in range(n):
    id=int(input("Enter the id:"))
    qty=int(input("Enter the quantity :"))
    if id==101:
        amt=20*qty
        print(amt)
    elif id==102:
        amt1=40*qty
        print(amt1) 
    elif id==103:
        amt2=50*qty
        print(amt2)
    elif id==104:
        amt3=70*qty
        print(amt3)
    else :
        print("Invalid choice!!")    

f_amt=amt+amt1+amt2+amt3
print("total amount payable:",f_amt)

cash=int(input("Total cash received:"))
change=cash-f_amt
print("change given :",change)
=======
print("id               product name            price")
print("101                   lays                 20")
print("102                  kurkere               40")
print("103                  biscuit                50")
print("104                   cake                  70")

amt=0
amt1=0
amt2=0
amt3=0



n=int(input("Enter the number of products :"))
for i in range(n):
    id=int(input("Enter the id:"))
    qty=int(input("Enter the quantity :"))
    if id==101:
        amt=20*qty
        print(amt)
    elif id==102:
        amt1=40*qty
        print(amt1) 
    elif id==103:
        amt2=50*qty
        print(amt2)
    elif id==104:
        amt3=70*qty
        print(amt3)
    else :
        print("Invalid choice!!")    

f_amt=amt+amt1+amt2+amt3
print("total amount payable:",f_amt)

cash=int(input("Total cash received:"))
change=cash-f_amt
print("change given :",change)
>>>>>>> 495afe01934516b77946be98f0aea5f6b92809b4
