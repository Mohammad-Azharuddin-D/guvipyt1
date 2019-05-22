a=list()
a=input().split()
n,k=input().split()
k=int(k)
s=0
for i in range(0,k):
    s=s+int(a[i])
print(s)
