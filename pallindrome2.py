# pallindrome check
num=int(input("Enter a value: "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10 + dig
    num=num//10
if(temp==rev):
    print("Pallindrome Number")
else:
    print("Not a Pallindrome Number")