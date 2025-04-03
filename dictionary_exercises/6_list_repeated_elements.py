#6- Check if a list contains repeated elements.

def return_if_has_repeated_elements(list_data):
    list_set=set(list_data)
    if len(list_data) != len(list_set):
        return True
    else:
        return False

def main():
    list_data=[1,2,3,4,5]
    has_repeated=return_if_has_repeated_elements(list_data)
    if has_repeated == True:
        print("The list has repeated elements")
    else:
        print("The list does not have repeated elements")

main()


