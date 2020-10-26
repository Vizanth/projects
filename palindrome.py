num=int(input("Enter  number"))
x=num
new=0
while(num>0):
    div=num%10
    new=new*10+div
    num=num//10
if (x==new):
    print("number is palndrom")
else:
    print("number is not palndrom")
