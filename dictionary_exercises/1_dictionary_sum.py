# grades={
#     "pepe":{
#         "mathematics":5,
#         "spanish":4
#     },
#      "juan":{
#          "mathematics":3,
#          "spanish":10
#     }
# }

# keys=list(grades.keys())
# values=list(grades.values())
# items=list(grades.items())

# pepe_grades=grades.get("pepe")

# #print(keys)
# print("-----")
# #print(values)
# print("-----")
# #print(items)

# pepe_mathematics_grades=pepe_grades.get("mathematics")
# print(pepe_mathematics_grades)

# list_data=[("pepe",36),("juan",40)]

# dict_data=dict(list_data)
# print(dict_data)




#1- Sum the values of a dictionary.
def sum_dictionary_values(dictionary):
    sum_val=0
    for key in dictionary:
        sum_val += dictionary.get(key)
    return sum_val

def sum_dictionary_values_2(dictionary):
    sum_val=0
    for value in dictionary.values():
        sum_val += value
    return sum_val

def sum_dictionary_values_3(dictionary):
    return sum(dictionary.values())
 
    












