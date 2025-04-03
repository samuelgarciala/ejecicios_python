# 6 - Algorithm that reads two numbers and tells us which one is greater or if they are equal (remember to use the conditional structure).

def start_message():
    print("Enter a number")

def input_number():
    number = int(input())
    return number

def compare_two_numbers(number_1, number_2):
    if number_1 > number_2:
        print(f"The number {number_1} is greater than {number_2}")
    elif number_2 == number_1:
        print(f"Both numbers are equal")
    else:
        print(f"The number {number_2} is greater than {number_1}")

def main():
    start_message()
    number_1 = input_number()
    start_message()
    number_2 = input_number()
    compare_two_numbers(number_1, number_2)

main()
