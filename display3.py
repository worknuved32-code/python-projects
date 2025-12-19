<<<<<<< HEAD
import array as arr
a=arr.array('i',map(int,input("Enter the array:").split()))
print("Original array :",a)
print("1.append\n"
      "2.remove\n"
      "3.reverse\n"
      "4.sort\n"
      "5.pop\n"
      "6.exit")
while(True):
    choice=int(input("Enter your choice :")) 
    if choice==1:
        n=int(input("Enter the element :"))
        a.append(n)
        print(a)
    elif choice==2:
        n=int(input("Enter the element :"))
        a.remove(n)
        print(a)
    elif choice==3:
        a.reverse()
        print(a)
    elif choice==4:
        a.sorted()
        print(a)
    elif choice==5:
        a.pop()
        print(a)    
    elif choice==6:
        print("Exiting bye!!!")
        exit()
    else:
        print("Invalid choice!!")



=======
import array as arr
a=arr.array('i',map(int,input("Enter the array:").split()))
print("Original array :",a)
print("1.append\n"
      "2.remove\n"
      "3.reverse\n"
      "4.sort\n"
      "5.pop\n"
      "6.exit")
while(True):
    choice=int(input("Enter your choice :")) 
    if choice==1:
        n=int(input("Enter the element :"))
        a.append(n)
        print(a)
    elif choice==2:
        n=int(input("Enter the element :"))
        a.remove(n)
        print(a)
    elif choice==3:
        a.reverse()
        print(a)
    elif choice==4:
        a.sort()
        print(a)
    elif choice==5:
        a.pop()
        print(a)    
    elif choice==6:
        print("Exiting bye!!!")
        exit()
    else:
        print("Invalid choice!!")



>>>>>>> 495afe01934516b77946be98f0aea5f6b92809b4
