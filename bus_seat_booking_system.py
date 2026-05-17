bus_seats=('1a','1b','1c','1d','2a','2b','2c','2d','3a','3b','3c','3d','4a','4b','4c','4d','5a','5b','5c','5d','6a','6b','6c','6d','7a','7b','7c','7d','8a','8b','8c','8d','9a','9b','9c','9d','10a','10b','10c','10d')
reserved_seat_details=()
reserved_seats=()

def int_error(var):
    while True:
        try:
            value=int(input(f'Enter {var}:'))
        except ValueError:
            print("Enter valid input!")
        else:
            return value

def display_seats():
    print('W-window seats')
    for seats in range(1,10):
        print(f'W {seats}a {seats}b    {seats}c {seats}d W')

def display_available_seats():
    count=1
    for seat in bus_seats:
        if seat in reserved_seats:
            reserve_status='X'
        else:
            reserve_status=seat
        if count%4!=0:
            print(f'{reserve_status}',end=' ')
        else:
            print(reserve_status)
        count+=1

def reserve_ticket():
    name=input('Enter name of the passenger:')
    age=int_error('age')
    # UnboundLocalError occurs when assignment is done to a var outside a func, no matter where it is. adding global will let the interpreter know that the var is global
    global reserved_seat_details, reserved_seats
    display_seats()
    while True:
        seat_no=input('Enter seat no:').lower()
        if seat_no not in bus_seats:
            print('''Invalid seat number
Enter a valid seat number!''')
        elif seat_no in reserved_seats:
            print(f'''{seat_no} is already reserved
Please enter another sit no''')
        else:
            break
    reserved_seat_details+=((seat_no,name,age),)
    reserved_seats+=(seat_no,)
    print(f"Seat {seat_no} is reserved on {name}'s name")

def cancel_ticket():
    print(1)
    global reserved_seats,reserved_seat_details
    while True:
        seat_no=input('Enter seat no:').lower()
        if seat_no not in bus_seats:
            print('''Invalid seat number
Enter a valid seat number!''')
            continue
        if seat_no not in reserved_seats:
            print(f'''{seat_no} is not reserved
Please enter another sit no''')
            continue
        else:
            reserved_seats=list(reserved_seats)
            reserved_seats.pop(reserved_seats.index(seat_no))
            reserved_seats=tuple(reserved_seats)
            reserved_seat_details=list(reserved_seat_details)
            for seat,count in zip(reserved_seat_details,range(40)):
                if seat[0]==seat_no:
                    reserved_seat_details.pop(count)
            reserved_seat_details=tuple(reserved_seat_details)
            break
    print(f'{seat_no} is cancelled')

def search_passenger():
    global reserved_seat_details
    while True:
        name=input('Enter name of the passenger:')
        for passenger,count in zip(reserved_seat_details,range(40)):
            if passenger[1]==name:
                reserved_seat_details=list(reserved_seat_details)
                reserved_seat_details.pop(count)
                reserved_seat_details=tuple(reserved_seat_details)
                print(f'{name} has a seat booked in {passenger[0]}')
                break
        else:
            print(f'{name} does not exist in the passenger list\nEnter a valid name')
        break


# # for i in range(2):
reserve_ticket()
# print(reserved_seat_details)
# print(reserved_seats)
display_available_seats()