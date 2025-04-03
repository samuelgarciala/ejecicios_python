# 4 - Design a program that asks the user for their age,
# and then indicates whether they are of legal age or underage.

def input_data():
    print("Enter your age:")
    age = int(input())
    return age

def is_of_legal_age(age):
    if age >= 18:
        print("You are of legal age.")
    else:
        print("You are underage.")

def main():
    age = input_data()
    is_of_legal_age(age)

main()