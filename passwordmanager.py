import hashlib
import getpass

# Setting up the password manager dictionary
passwordManager = {}

def createAccount():
    # Prompting the user
    username = input("Enter your chosen username: ")
    password = input ("Enter your chosen passsword: ")
    
    hashedPassword = hashlib.sha256(password.encode()).hexdigest() # Uses the getpass library to hide the plaintext password, then the hashlib library to hash the password using the sha256 algorithm
    passwordManager[username] = hashedPassword # Adding this new account to the passwordManager dictionary as a key value pair
    print("Account created successfully") # Give visual feedback to the user as proof of their account creation
    
def login():
    username = input("Please enter your username: ") 
    password = getpass.getpass("Please enter your password: ")
    
    hashedPassword = hashlib.sha256(password.encode()).hexdigest()
    
    # Does the username and hashed password match a key pair within the passwordManager dictionary?
    if username in passwordManager.keys() and passwordManager[username] == hashedPassword:
        print("Login successful")
        print(hashedPassword)
    else:
        print("Invalid username or password")
        
def main():
    while True:
        # Prompts the user to enter the integer corresponding with the option of their choice
        choice = int(input("Would you like to create an account[1], login[2] or exit[0]: "))
        
        if choice == 1:
            createAccount()
            
        elif choice == 2:
            login()
        
        elif choice == 0:
            break
        
        else:
            print("Invalid input")
            
main()