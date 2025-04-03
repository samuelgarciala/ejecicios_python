#5- Find the most repeated element in a tuple.
#only works for a single element

def count_characters_in_tuple(tuple_data):
    dictionary={}
    for character in tuple_data:
        if character not in dictionary:
            dictionary[character]=1
        else:
            dictionary[character]+=1
    return dictionary


def largest_element_of_dictionary(dictionary):
    largest_element=None
    largest_value=0
    for key,value in dictionary.items():

        if value > largest_value:
            largest_value=value
            largest_element=key

    return largest_element

def main():
    tuple_data = (1,2,3,4,5,6,6,7)
    tuple_dictionary=count_characters_in_tuple(tuple_data)
    largest_element=largest_element_of_dictionary(tuple_dictionary)
    print(largest_element)

main()




