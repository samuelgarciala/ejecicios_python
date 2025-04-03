# 7 - Design an algorithm that asks for three numbers; if the first one is negative, it should print the product of all three
# and if not, it will print the sum.

def number_message(message):
    print(message)

def input_data():
    number = float(input())
    return number

def data_check(first_number, second_number, third_number):
    if first_number < 0:
        result_sum_or_product = first_number * second_number * third_number
        return result_sum_or_product
    else:
        result_sum_or_product = first_number + second_number + third_number
        return result_sum_or_product

def output_message(result_sum_or_product, first_number, second_number, third_number):
    if result_sum_or_product == (first_number + second_number + third_number):
        print(f"The sum of the numbers is: {result_sum_or_product}")
    else:
        print(f"The product of the numbers is: {result_sum_or_product}")

def main():
    number_message("Enter the first number")
    number_1 = input_data()
    number_message("Enter the second number")
    number_2 = input_data()
    number_message("Enter the third number")
    number_3 = input_data()
    sum_or_product = data_check(number_1, number_2, number_3)
    output_message(sum_or_product, number_1, number_2, number_3)

main()
