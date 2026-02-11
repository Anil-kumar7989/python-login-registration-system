users = {
         "Anilkumar" : "Anil123",
         "Shivakumar" : "Shiv@1234",           #first check how are all in users database
         "Udaykiran" : "Uday123"
}

def sign_in():
    username = input("Enter Username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print ("Login succefully")
    else:
        print("Invalid Useername and password")    
# if you don't have account create an account 
def create_account():
    username = input("Create Username: ")
    password = input("Create password: ")

    if username in users:
        print("Username already exist try again")
        return
    if password in users.values():
        print("Password already used")
        return
# stored in users dictionary #
    users[username] = password 

    print("Account created successfully")
    print("Account saved in users list")


# =========================== Main program =====================

choice = input("Welcome to web page login!..Do you have an account? (yes/no): ").lower()

if choice == "yes":
    print("Sign in your account")
    sign_in()

elif choice == "no":
    print("First create an account")
    create_account()

else:
    print("Invalid choice")

print("\ncurrent Users in database: ")    
print(users)




