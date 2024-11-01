import random
import string

def generate_password(length, complexity):
    lower = string.ascii_lowercase  
    upper = string.ascii_uppercase  
    digits = string.digits          
    symbols = string.punctuation    
    
    # Based on complexity, adjust character pool
    if complexity == 1:
        char_pool = lower
    elif complexity == 2:
        char_pool = lower + upper
    elif complexity == 3:
        char_pool = lower + upper + digits
    else:
        char_pool = lower + upper + digits + symbols
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    # Get user input for length and complexity
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
        
        print("Select complexity level:")
        print("1 - Lowercase letters only")
        print("2 - Lowercase and Uppercase letters")
        print("3 - Letters and digits")
        print("4 - Letters, digits, and symbols")
        complexity = int(input("Enter the complexity level (1-4): "))
        if complexity < 1 or complexity > 4:
            print("Invalid complexity level.")
            return
        

        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter valid numbers for length and complexity.")

if __name__ == "__main__":
    main()
