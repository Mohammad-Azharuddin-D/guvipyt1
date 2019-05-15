number = int(input())
value = 0
for i in range(2,number):
    if (number % i == 0):
        value = value + 1
if(value >= 1):
    print("no")
else:
    print("yes")   
