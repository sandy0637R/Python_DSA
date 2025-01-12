num = int(input("Enter a positive no"))

result=1

if(num<0):
    print("enter a positive no")
elif(num==0 or num==1):
     print(f"factorial of {num} is 1")
else:
     for i in range(1,num+1):
          result*=i
     print(f"the factorial of {num} is {result}")
          