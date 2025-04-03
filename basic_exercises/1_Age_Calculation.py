# Write a program that asks for the current year and the user's birth year.
# It should calculate their age, assuming the user has already had their birthday this year.

def input_current_year():
    print(f"Enter the current year")
    current_year = int(input())
    return current_year

def input_birth_year():
    print(f"Enter your birth year")
    birth_year = int(input())
    return birth_year

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

def output_data(age):
    print(f"Your age is: {age}")

def main():
    current_year = input_current_year()
    birth_year = input_birth_year()
    age = calculate_age(current_year, birth_year)
    output_data(age)

main()



