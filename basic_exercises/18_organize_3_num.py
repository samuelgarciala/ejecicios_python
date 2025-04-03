# 18 - Program that reads 3 numbers from the keyboard and displays them in sorted order.

def sort_3_numbers(numbers):
    highest_number = None
    middle_number = None
    lowest_number = None
    
    for number in numbers:
        if highest_number is None or number > highest_number:
            lowest_number = middle_number
            middle_number = highest_number
            highest_number = number
        elif middle_number is None or number > middle_number:
            lowest_number = middle_number
            middle_number = number
        else:
            lowest_number = number

    return [lowest_number, middle_number, highest_number]

def main():
    numbers = []
    for entered_number in range(1, 4):
        number = int(input(f"Enter the {entered_number}° number: "))
        numbers.append(number)
    
    sorted_list = sort_3_numbers(numbers)
    
    print(sorted_list)
    
main()


    
    