s,y,c=input().split()
s=int(s)
y=int(y)
c=int(c)
if(s>=y and s>=c):
    print(s)
elif(y>=s and y>=c):
    print(y)
else:
    print(c)
