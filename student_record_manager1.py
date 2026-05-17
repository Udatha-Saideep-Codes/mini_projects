# global variables declaration 
students={}
subjects_for_new_student={'ATCD':0,'DBMS':0,'IAI':0,'OS':0,'FPP':0}
ATCD,DBMS,IAI,OS,FPP={},{},{},{},{}
# subjects are also stored as strings so that they can be displayed while showing subject wise marks
subjects_as_strings=['ATCD','DBMS','IAI','OS','FPP']
subjects=[ATCD,DBMS,IAI,OS,FPP]
def int_error(var):
    while True:
        try:
            x=int(input(f"Enter {var}:"))    
        except ValueError:
            print('Enter a valid input!')
        else:
            return x

def add_student():
    roll_number=input("Enter the roll number of the student:")
    if roll_number in students:
        while(1):
            print(f'''there is already a student with roll number {roll_number}''')
            roll_number=input('Please enter a new roll number')
            if roll_number not in students:
                break

    #for a new student attendance is 0 initially
    attendance=0
    name=input('Enter name of the student:')
    phone=int_error('Phone number')
    students[roll_number]={'name':name,'attendance':attendance,'phone':phone,'subjects':subjects_for_new_student}
    print('Student added')

def delete_student():
    roll_number=input('Enter the roll number of the  student:')
    deleted_student=students.pop(roll_number)
    print(f'student {deleted_student['name']} is removed from the student list')

def update_marks():
    roll_number=input('Enter roll number of the student:')
    # students[roll_number]['subjects'] is a nested indexing and used to access subject which is a sub-sub dictionary of students 
    if roll_number not in students:
            while(1):
                print(f'''there is no student with roll number {roll_number}
the list of student roll numbers are {list(students.keys())}''')
                roll_number=input('Please enter a valid roll number')
                if roll_number in students:
                    break
    for student_subject,subject in zip(students[roll_number]['subjects'],subjects):
        marks=int(input(f'Enter marks of {student_subject}:'))
        students[roll_number]['subjects'][student_subject]=marks
        subject[roll_number]=marks
    print(f'{roll_number} marks are updated')

def search_student():
    search_student_name=(input('Enter the name of the student:'))
    for roll_number,name in students.items():
        if name['name']==search_student_name:
            print(f'''Student found
name:{search_student_name}
attendance:{name['attendance']}
phone:{name['phone']}''')

def display_all_students():
    for roll_number,details in students.items():
        print(f'{roll_number}:{details['name']}')

def display_subject_wise_marks():
    for subject,subject_string in zip(subjects,subjects_as_strings):
        print(f'{subject_string} Marks')
        for roll_number,subject_marks in subject.items():
            print(f'roll number {roll_number} has got {subject_marks}')

def number_of_students_for_operation():
    number_of_students=int_error('Number of students')

# Display choices and then call the functions
while(1):
    print(f'''
Welcome to student record manager
This program can perform the following operations:
    1. add student
    2. update marks of student
    3. search student
    4. display all students
    5. display subject wise marks 
    6. delete a student
    7. Quit program
''')
    
    while(1):
        try:
            choice=int(input('Enter your choice of operation:'))
        except ValueError:
            print('Enter a valid choice')
        else:
            print(f'You chose operation {choice}')
            break
    match choice:
        case 1:
            no_of_students=number_of_students_for_operation()
            for student in range(no_of_students):
                print(f'student {student}:')
                add_student()
                print()
            print(f'{no_of_students} students are added')
        case 2:
            no_of_students=number_of_students_for_operation()
            for student in range(no_of_students):
                print()
                print(f'Enter marks of student {student}:')
                update_marks()
                print()
            print(f'marks of {no_of_students} are updated')
        case 3:
            search_student()
            print()
        case 4:
            display_all_students()
            print()
        case 5:
            display_subject_wise_marks()
            print()
        case 6:
            delete_student()
            print()
        case 7:
            break  