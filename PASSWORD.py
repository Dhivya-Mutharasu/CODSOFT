import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length using
    a combination of uppercase, lowercase, digits, and special characters.
    
    Parameters:
    length (int): The length of the password to be generated.
    
    Returns:
    str: The generated password.
    """
    # Define the characters to be used in the password
    char = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    pwd= ''.join(random.choice(char) for _ in range(length))
    
    return pwd

def main():
    """
    Main function to prompt the user for input and display the generated password.
    """
    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the password
        pwd = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {pwd}")
    
    except ValueError:
        print("Please enter a valid integer for the password length.")

# Run the main function
if __name__ == "__main__":
    main()
