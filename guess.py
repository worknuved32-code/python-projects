word="darkness"
print("the more of this there is,the less you see.what is it?")
guess=""
count=0

while guess!=word:
    guess=input("Enter the answer :")
    count=count+1
    

print("You win!!!!")
print("total number of guess",+count)
