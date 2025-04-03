#23- Program that prints the multiplication table of an integer (between 1 and 10).

def input_message():
    print("Enter the number for which you want to get the multiplication table")
    
def data_input():
    entered_number = int(input())
    return entered_number

def multiply_i_from_1_to_10(entered_number):
    for i in range(1, 11):
        if entered_number == i:
            result_1 = 1 * i    
            result_2 = 2 * i
            result_3 = 3 * i
            result_4 = 4 * i
            result_5 = 5 * i
            result_6 = 6 * i
            result_7 = 7 * i
            result_8 = 8 * i
            result_9 = 9 * i
            result_10 = 10 * i
            
            print(f"0x{i} = 0")
            print(f"1x{i} = {result_1}")
            print(f"2x{i} = {result_2}")
            print(f"3x{i} = {result_3}")
            print(f"4x{i} = {result_4}")
            print(f"5x{i} = {result_5}")
            print(f"6x{i} = {result_6}")
            print(f"7x{i} = {result_7}")
            print(f"8x{i} = {result_8}")
            print(f"9x{i} = {result_9}")
            print(f"10x{i} = {result_10}")
            
def main():
    input_message()
    entered_number = data_input()
    multiply_i_from_1_to_10(entered_number)

main()
