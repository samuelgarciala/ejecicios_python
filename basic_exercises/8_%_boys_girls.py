# 8 - A school wants to know the percentage of boys and the percentage of girls in the current class. Design an algorithm for this purpose.

def start_message(message):
    print(message)

def input_total_boys_girls():
    total_students = int(input())
    return total_students

def define_percentage_boys(total_boys, total_students):
    percentage_boys = total_boys / total_students * 100
    return percentage_boys

def define_percentage_girls(percentage_boys):
    percentage_girls = 100 - percentage_boys
    return percentage_girls

def final_message(percentage_boys, percentage_girls):
    print(f"The percentage of boys is {percentage_boys} %")
    print(f"The percentage of girls is {percentage_girls} %")

def main():
    start_message("Enter the total number of boys")
    total_boys = input_total_boys_girls()
    start_message("Enter the total number of girls")
    total_girls = input_total_boys_girls()   
    total_students = total_girls + total_boys
    percentage_boys = define_percentage_boys(total_boys, total_students)
    percentage_girls = define_percentage_girls(percentage_boys)
    
    final_message(percentage_boys, percentage_girls)

main()
