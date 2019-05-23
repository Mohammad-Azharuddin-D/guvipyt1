n=int(input())
temp=n
add=0
while(temp>0):
    val=temp%10
    val=val**3
    add=add+val
    temp//=10
if(n==add):
    print("yes")

else:
    print("no")
