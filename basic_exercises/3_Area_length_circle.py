# 3 - Design an application that calculates the length and area of a circle.

def calculate_area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area

def calculate_circumference_length(radius):
    length = 2 * 3.14 * radius
    return length

def input_data():
        print("Enter radius:")
        radius = int(input())
        return radius

def output_data(area, length):
    print(f"The area is {area} and the length is {length}")

def main():
    r = input_data()
    area = calculate_area_of_circle(r)
    length = calculate_circumference_length(r)
    output_data(area, length)

main()




    