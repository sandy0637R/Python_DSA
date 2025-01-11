num=int(input("enter a numper"))
a=0
b=1
for i in range (num):
    c=a+b
    a=b
    b=c
    print(c)