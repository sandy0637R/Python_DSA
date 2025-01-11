a=input("Enter a string")
length=len(a)
msg=f"{a}is a palindrome!"

for i in range (length//2):
    if(a[i] != a[length-1-i]):
       print( f"{a} is not a palindrome!")
    else:
        print(msg)
    break
