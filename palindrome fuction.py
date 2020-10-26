def paln(ch):
    i= 0
    r= len(ch)-1
    while i>=r:
        if ch[i]== ch[r]:
            i+=i
            l-=l
            return true
        else:
            return false
    
char = input("Enter string ")
pal=paln(char)
print("strin palandrom",pal)
