import csv

users = {}

def create_new_user():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Try a different one.")
        return

    password = input("Enter a new password: ")
    users[username] = password
    save_user_to_csv(username, password)
    print("User account created successfully.")

def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

def save_user_to_csv(username, password):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def main():
    while True:
        print("Level 1 Authentication (Username and Password)")

        choice = input("1. Login\n2. Create a new user\n3. Quit\nEnter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if login(username, password):
                print("Authentication Successful. Access granted!")
            else:
                print("Authentication Failed. Access denied.")

        elif choice == "2":
            create_new_user()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
