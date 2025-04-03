#24- Create an algorithm that sums the even natural numbers that are less than a number entered via the keyboard.

def sum_of_even_integers(entered_number):
    total_sum = 0
    for i in range(entered_number):
        if i % 2 == 0:
            total_sum = i + total_sum
    return total_sum

def output_data(entered_number, total_sum):
    print(f"The sum of even integers less than {entered_number} = {total_sum}")
    
def input_data():
    entered_number = int(input("Enter a number: "))
    return entered_number

def main():
    entered_number = input_data()
    total_sum = sum_of_even_integers(entered_number)
    output_data(entered_number, total_sum)
    
main()
