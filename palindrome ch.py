ch=input("Enter character")
x=len(ch)-1
rev=''
while(x>=0):
    rev=rev+ch[x]
    x=x-1
if (ch==rev):
    print ("palindrome char")
else:
    print("Not palindrome char")
    
    
