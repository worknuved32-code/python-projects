num1=float(input("Enter the first number :")) 
num2=float(input("Enter the second number :"))
op=input("Enter your choice ('+,%,*,/,-') :")
 

if op == "+":
    print("Sum :",+(num1+num2))
elif op == "-":
    print("difference :",+(num1-num2))
elif op == "*":
    print("product:",+(num1*num2))
elif op == "/":
    print("qoutient :",+(num1/num2))
elif op == "%":
    print("remainder :",+(num1%num2))
else :
    print("Invalid choice")

        
    