a,b=map(int,input().split())
for i in range(a,b):
  s=0
  temp=i
  while(temp>0):
    c=temp%10
    s=s+c**3
    temp=temp//10
  if(i==s):
    print(s,end=" ")
