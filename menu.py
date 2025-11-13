while True:
    print("---------Simple Menu----------")
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice=int(input("Enter your choice :"))
    if choice==5:
        print("Exiting.......bye!!!")
        break
    a=float(input("Enter the first number :"))
    b=float(input("Enter the second number :"))
    if choice==1:
       print("Result :",a+b)
    elif choice==2:
       print("Result :",a-b)
    elif choice==3:
      print("Result :",a*b)   
    elif choice==4:
       print("Result :",a/b)
    else :
       print("Invalid choice!!! \n try again")     

    