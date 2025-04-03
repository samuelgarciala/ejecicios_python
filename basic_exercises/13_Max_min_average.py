# 13 - Algorithm that reads integers until 0 is entered, and then displays the maximum, minimum, and average of all of them.
# Think about how we should initialize the variables.

def input_data_and_exit_with_0():  
    counter = 0
    
    while True:
        print('Enter a number or enter "0" to display the results of all previously entered numbers')
        entered_number = float(input())
        if counter == 0 and entered_number == 0:
            print("No data has been entered, please start again")
            entered_number = None
            
        if entered_number == 0:
            break
        
        number_list.append(entered_number)
        counter += 1
    return number_list

def calculate_maximum(number_list):
    maximum_number = max(number_list)
    return maximum_number

def calculate_minimum(number_list):
    minimum_number = min(number_list)
    return minimum_number

def calculate_average(number_list):
    average = sum(number_list) / len(number_list)
    return average

def output_data(maximum_number, minimum_number, average):
    print(f"The highest number is: {maximum_number}.")
    print(f"The lowest number is: {minimum_number}.")
    print(f"The average is: {average}.")

def main():
    number_list = input_data_and_exit_with_0()
    maximum_number = calculate_maximum(number_list)
    minimum_number = calculate_minimum(number_list)
    average = calculate_average(number_list)
    output_data(maximum_number, minimum_number, average)

number_list = []
main()
