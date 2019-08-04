a,b=map(int,input().split())
for i in range(a,b):
    s=0
    temp=i
    while(temp>1):
        d=temp%10
        s=s+d**3
        temp=temp//10
        if(i==s):
            print(s,end=" ")
        else:
            continue        
