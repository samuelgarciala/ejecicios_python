# 11 - The task is to represent the algorithm that calculates the sum of the first N natural numbers. N will be read from the keyboard.

def input_data():
    number = int(input("Enter the number N: "))
    return number
    

def calculate_sum(number):
    sum_value = 0
    for i in range(1, number + 1):
        sum_value = sum_value + i
    return sum_value

def output_data(sum_value):
    print(f"{sum_value}")

def main():
    number = input_data()
    sum_value = calculate_sum(number)
    output_data(sum_value)
    
main()
