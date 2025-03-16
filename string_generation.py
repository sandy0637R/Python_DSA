def generate_string(n):
    a = "a"
    b = "b"
    
    if n > 0:
        return a * n + b * n 

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a number: "))
            result = generate_string(n)
            print(f"Generated string for n={n} = {result}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for n.")
