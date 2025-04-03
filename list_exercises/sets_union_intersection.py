def union_of_2_set_elements(set_1, set_2):
    union = set_1.union(set_2)
    # union = set_1 | set_2
    return union

def intersection_of_2_set_elements(set_1, set_2):
    intersection = set_1.intersection(set_2)
    # intersection = set_1 & set_2
    return intersection

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7]

set_1 = set(list_1)
set_2 = set(list_2)

def main():
    intersection = intersection_of_2_set_elements(set_1, set_2)
    union = union_of_2_set_elements(set_1, set_2)
    print(f"intersection: {intersection}")
    print(f"union: {union}")

main()