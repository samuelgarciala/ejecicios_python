# 10 - Develop an algorithm that calculates the square of the first 9 natural numbers.

def square_of_natural_numbers_up_to_9():        
    for natural_number in range(1, 10):
        square = natural_number ** 2
        print(f"The square of the number {natural_number} is: ({square})")


def main():
    square_of_natural_numbers_up_to_9()

main()
