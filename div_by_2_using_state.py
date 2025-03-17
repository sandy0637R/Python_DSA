def div_by_2(number):
    state ="q0" if number[-1] in "02468" else "q1"
    
    return state == "q0"

if __name__=="__main__":
    number=input("enter a decimal no").strip() 
    
    if div_by_2(number):
        print(f"the no {number} is divisible by 2")
    else:
        print(f"the no {number} is not divisible by 2")
    
        