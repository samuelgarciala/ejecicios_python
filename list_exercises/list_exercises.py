#1- Implement a function that counts the frequency of elements in a list.

def element_frequency_counter(list_data, element):
    counter = 0
    for list_element in list_data:
        if element == list_element:
            counter += 1
    return counter

#2- Implement a function that calculates the sum of the elements of a numeric list.

def sum_list(list_data):
    sum_element = 0
    for list_element in list_data:
        sum_element += list_element
    return sum_element

#3- Implement a function that removes all occurrences of an element in a list.

def element_remover(list_data, element):
    new_list = []
    for list_element in list_data:
        if element != list_element:
            new_list.append(list_element)
    return new_list

#4- Implement a function that allows extending a list. The function must receive another list
#as a parameter and return the original list with the elements of the list passed as
#parameter.

def extend_list(original_list, copy_list):
    for list_element in copy_list:
        original_list.append(list_element)

#5- Implement a function that allows copying the elements of a list.

def copy_list(list_data):
    copy_list_data = []
    for list_element in list_data:
        copy_list_data.append(list_element)
    
    return copy_list_data


#6- Implement a function that allows inverting the elements of a list.

def invert_elements(list_data):
    new_list = []
    for i in range(len(list_data) - 1, -1, -1):
        new_list.append(list_data[i])
    return new_list

#7- Write a function that returns the maximum value of a numeric list.

def max_value_list(list_data):
    if list_data == []:
        return None
    
    largest_number = list_data[0]
    for list_number in list_data:
        if list_number > largest_number or largest_number == None:
            largest_number = list_number        
    return largest_number

#8- Create a function that removes duplicates from a list. It must receive a list as a parameter and return a new list without repeated elements.

def remove_duplicates_list(list_data):
    list_without_duplicates = []
    for number in list_data:
        if number not in list_without_duplicates:
            list_without_duplicates.append(number)
    
    return list_without_duplicates


#9- Create a function that returns the even numbers of a list.

def even_numbers_list(list_data):
    even_numbers_list_data = []
    for list_number in list_data:
        if list_number % 2 == 0:
            even_numbers_list_data.append(list_number)
    
    return even_numbers_list_data

#10- Implement a function that returns the intersection between two lists.

def find_intersection_between_two_lists(list_1, list_2):
    matching_numbers_list = []
    for number in list_1:
        if number in list_2 and number not in matching_numbers_list:
            matching_numbers_list.append(number)
    
    return matching_numbers_list




list_data = [1, 2, 2]
list_data_2 = [3, 2, 1]
list_remove = find_intersection_between_two_lists(list_data, list_data_2)

print(list_remove)