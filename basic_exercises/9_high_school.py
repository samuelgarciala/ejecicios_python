# 9 - Algorithm that tells us if a person can access a higher education course or not. To access a higher course, if you have a high school diploma, you can enter directly. If not, you can access if you pass an entrance exam.

def ask_high_school_diploma():
    attempts = 0
    correct_input = False

    while attempts < 3 and correct_input == False:
        attempts += 1
        print("Do you have a high school diploma, yes or no?")
        has_high_school_diploma = input()
        if has_high_school_diploma == "yes":
            print("You can take the higher education course")
            raise SystemExit
        elif has_high_school_diploma == "no":
            correct_input = True
        else:
            correct_input = False
            print("You have entered an incorrect value")
            if attempts == 3:
                print("Closing program")
                raise SystemExit

def check_entrance_exam():
    attempts = 0
    while attempts < 3:
        attempts += 1
        
        print("Did you pass the entrance exam, yes or no?")
        entrance_exam = input()
        
        if entrance_exam == "yes":
            print("You can take the higher education course")
            break
        
        elif entrance_exam == "no":
            print("You cannot take the higher education course")
            break
        
        else:
            print("You have entered an incorrect value")

def closing_program_message():
    print("Closing the program")

def main():
    ask_high_school_diploma()
    check_entrance_exam()
    closing_program_message()

main()
