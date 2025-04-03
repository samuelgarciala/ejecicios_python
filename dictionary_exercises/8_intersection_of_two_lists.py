#8 A gym records the names of clients who attend each day. Create a function that compares the attendance of two days and shows the clients who attended both days.

attendance_list_day_1=["juan","jose","samuel","daniela","julia"]
attendance_list_day_2=["manuela","juan","daniela","pedro"]

def intersection_of_two_lists(attendance_list_day_1,attendance_list_day_2):
    day_1_set=set(attendance_list_day_1)
    day_2_set=set(attendance_list_day_2)
    intersection= day_1_set & day_2_set
    return list(intersection)
    
def test():
    attendance_list_day_1=["juan","jose","samuel","daniela","julia"]
    attendance_list_day_2=["manuela","juan","daniela","pedro"]    
    intersection=intersection_of_two_lists(attendance_list_day_1,attendance_list_day_2)
    print(intersection)

test()