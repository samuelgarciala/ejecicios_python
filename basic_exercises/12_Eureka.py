# 12 - Given that the correct password is "eureka", write an algorithm that asks for a password. 
# We only have 3 attempts to guess it correctly. If we fail all 3 attempts, a message will indicate that we have used up all attempts. 
# If we enter the correct password, the program will exit immediately.

def request_eureka_password():
    print("Enter the client password")

def check_eureka_password_three_attempts(password):
    for i in range(1, 4):
        attempt = input()
        if attempt == password:
            print("Welcome")
            break
        else:
            print(f"Incorrect password, attempts {i}/3")
            if i == 3:
                print("Closing program")
            
def main():
    password = "eureka"
    request_eureka_password()
    check_eureka_password_three_attempts(password)

main()
