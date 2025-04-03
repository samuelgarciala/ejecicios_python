# 14 - Algorithm that displays the count of numbers that are multiples of 2 or 3 between 1 and 100.

def multiples_of_2_or_3():
    multiples_count = 0
    for i in range(1, 101):
        if i % 2 == 0 or i % 3 == 0:
            multiples_count += 1
    return multiples_count
        
def output_data(multiples_count):
    print(f"The result is: {multiples_count}")
    
def main():
    multiples_count = multiples_of_2_or_3()
    output_data(multiples_count)
    
main()
