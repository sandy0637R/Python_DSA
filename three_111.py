def check(sequence):
    count = 0  

    for digit in sequence:
        if digit == "1":
            count += 1
            if count == 3:  
                return True
        else:
            count = 0  
    
    return False  

def check_input():
    user_input = input("Enter a string over 0s and 1s: ")
    if check(user_input):
        print("Accepted")
    else:
        print("Rejected")

if __name__ == "__main__":
    check_input()
