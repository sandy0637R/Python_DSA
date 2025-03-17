def check_end(a):
    state=0
    
    for char in a:
        if state== 0 and char =="1":
            state=1
        elif state==1 and char=="0":
            state=2
        elif state==2 and char=="1":
            state=3
        else:
            state=0
    return state==3

def check ():
    a=input("Enter string in 1s and 0s:")
    if check_end(a):
        print("accepted")
    else:
        print("rejected")    
        
if __name__=="__main__":
    check()
            