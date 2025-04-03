# 2 - Create a program that calculates the arithmetic mean of three values read from the keyboard,
# and displays the result on the screen.

def start_text():
        print(f"Enter your 3 numbers")
        
def input_number():
    number = int(input())
    return number

def calculate_mean(number_1, number_2, number_3):
    mean = (number_1 + number_2 + number_3) / 3
    return mean

def output_data(mean):
    print(f"The mean of the three numbers is: {mean}")

def main():
    start_text()
    number_1 = input_number()
    number_2 = input_number()
    number_3 = input_number()
    mean = calculate_mean(number_1, number_2, number_3)
    output_data(mean)

main()

    
    
    