#10- An institute records for each student their name and the grades of 5 subjects.
# It is necessary to return the students whose grade average does not exceed a given value.


student_grades={
    
    "student_1":{"mathematics":7,"physics":9,"chemistry":4,"spanish":7,"social studies":3},
    "student_2":{"mathematics":10,"physics":10,"chemistry":9,"spanish":9,"social studies":8},
    "student_3":{"mathematics":3,"physics":4,"chemistry":5,"spanish":8,"social studies":4},
}

def passed_failed_students(student_grades,minimum_grade):
    passed_students=[]
    failed_students=[]
    
    for student,subject_grade_values in student_grades.items():
        average= sum(subject_grade_values.values())/len(subject_grade_values.keys())

        if average >= minimum_grade:
            passed_students.append(student)
        else:
            failed_students.append(student)
    
    print(f"passed: {passed_students}")
    print(f"failed: {failed_students}")
    
def main():
    minimum_grade=int(input("enter minimum grade: "))
    passed_failed_students(student_grades,minimum_grade)
    
main()