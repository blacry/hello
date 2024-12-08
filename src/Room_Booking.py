import misc
import room_perks
import Bill
import rooms 
def room_booking():
    print('What kind of room do you want to book?')
    print('1.Single Room')
    print('2.Double Room')
    print('3.Twin Room')
    print('4.Family Room')
    print('5.Luxuary Room')
    print('if you want to know the perks of all the rooms, PRESS ENTER <==')
    
    room_choice=input('Enter your choice:')
    if room_choice:
        price,roomno = priceDetails(int(room_choice))
    else:
        room_perks.perks()
        room_booking()
    customer_name, customer_email, customer_phone, customer_check_in, customer_check_out = customerDetails()
    cid = c_id()
    
    import mysql.connector as sqlcon
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    query="insert into customerinfo values({},'{}','{}',{},'{}','{}')".format( cid, customer_name, customer_email, customer_phone, customer_check_in, customer_check_out)
    cursor.execute(query)
    con.commit()
    
    rooms.roomassigner(roomno,cid,customer_check_out)
    Bill.bill(cid,customer_name,customer_email,customer_phone,customer_check_in,customer_check_out,price)
def priceDetails(choice):
    if choice==1:
        a = input('Your room will be of ₹ 1000 , Press 1 to confirm & Press 2 to cancel')
        if int(a) == 1:
            room_no=rooms.roomfinder(choice)
            return 1000,room_no
        
        elif int(a) == 2:
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)

    if choice==2:
        a = input('Your room will be of ₹ 2000 , Press 1 to confirm & Press 2 to cancel ')
        if int(a) == 1:
            room_no=rooms.roomfinder(choice)
            return 2000,room_no
        elif int(a) == 2:
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)

    if choice==3:
        a = input('Your room will be of ₹ 4000 , Press 1 to confirm & Press 2 to cancel ')  
        if int(a) == 1:
            room_no=rooms.roomfinder(choice)
            return 4000,room_no
        elif int(a) == 2:
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)

    if choice==4:
        a = input('Your room will be of ₹ 6000 , Press 1 to confirm & Press 2 to cancel ')
        if int(a) == 1:
            room_no=rooms.roomfinder(choice)
            return 6000,room_no
        elif int(a) == 2:
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)
    if choice==5:
        a = input('Your room will be of ₹ 10000 , Press 1 to confirm & Press 2 to cancel ')
        if int(a) == 1:
            room_no=rooms.roomfinder(choice)
            return 10000,room_no
        elif int(a) == 2:
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)
    else:
        misc.correct(room_booking)
   

def customerDetails():
    while True:
        print('Enter your details')

        # Name
        name = input('Enter your name: ').strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        # Email
        email = input('Enter your email address: ').strip()
        if not ("@gmail.com" in email):
            print("Please enter a valid Gmail address.")
            continue

        # Phone
        phone = input('Enter your phone number (10 digits): ').strip()
        if not (phone.isdigit() and len(phone) == 10):
            print("Invalid phone number! It must be exactly 10 digits.")
            continue
        phone = int(phone)

        # Check-in and Check-out Dates
        check_in = input('Enter the check-in date (YYYY-MM-DD): ').strip()
        check_out = input('Enter the check-out date (YYYY-MM-DD): ').strip()

        # Confirmation of data
        print("\nPlease confirm your details:")
        print("Name: {}".format(name))
        print("Email: {}".format(email))
        print("Phone: {}".format(phone))
        print("Check-in Date: {}".format(check_in))
        print("Check-out Date: {}".format(check_out))

        confirmation = input("Is this information correct? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            break
        else:
            print("Let's re-enter your details.\n")

    return name, email, phone, check_in, check_out

def c_id():
    import random
    import mysql.connector as sqlcon
    
    cid=random.randint(10000000,99999999)

    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='swaraj_hotel',auth_plugin="mysql_native_password")
    cursor=con.cursor()

    check = "select c_id from customerinfo where c_id ={}".format(cid)
    cursor.execute(check)
    check = cursor.fetchall()

    if check:
         cid = c_id()

    return cid
        



''' 
    def bookRoom(room_no,name,email,phone,address,room_type,price,check_in,check_out,bill):
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("INSERT INTO room_booking(room_no,name,email,phone,address,room_type,price,check_in,check_out,bill) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(room_no,name,email,phone,address,room_type,price,check_in,check_out,bill))
    con.commit()
    cursor.close()
    con.close()
'''

'''
print('2.Check Room Availability')
print('3.Contact Us')
print('4.Provide Feedback')
print('5.View Feedback')
print('6.Exit')
choice=int(input('Enter your choice:'))
if choice==1:
    print('Enter the room number:')
    room_no=int(input())
    print('Enter the guest name:')
    name=input()
    print('Enter the age:')
    age=int(input())
    print('Enter the gender:')
    gender=input()
    print('Enter the email:')
    email=input()
    print('Enter the phone number:')
    phone=input()
    print('Enter the address:')
    address=input()
    print('Enter the room type:')
    room_type=input()
    print('Enter the price:')
    price=int(input())
    print('Enter the check in date:')
    check_in=input()
    print('Enter the check out date:')
    check_out=input()
    print('Enter the bill amount:')
    bill=int(input())
    print('Enter the feedback:')
    feedback=input()
    if feedback=='':
        print('Enter the feedback:')
        feedback=input()
    else:
        print('Thank you for providing feedback')
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("INSERT INTO room_booking(room_no,name,age,gender,email,phone,address,room_type,price,check_in,check_out,bill,feedback) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(room_no,name,age,gender,email,phone,address,room_type,price,check_in,check_out,bill,feedback))
    con.commit()
    cursor.close()
    con.close()
elif choice==2:
    print('Enter the room number:')
    room_no=int(input())
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM room_booking WHERE room_no=%s",(room_no))
    result=cursor.fetchall()
    for row in result:
        print('Room Number:',row[0])
        print('Name:',row[1])
        print('Age:',row[2])
        print('Gender:',row[3])
        print('Email:',row[4])
        print('Phone:',row[5])
        print('Address:',row[6])
        print('Room Type:',row[7])
        print('Price:',row[8])
        print('Check In:',row[9])
        print('Check Out:',row[10])
        print('Bill:',row[11])
        print('Feedback:',row[12])
    cursor.close()
    con.close()
elif choice==3:
    print('Email: swaraj@gmail.com')
    print('Phone: +91-9876543210')
elif choice==4:
    print('Enter the room number:')
    room_no=int(input())
    print('Enter the feedback:')
    feedback=input()
    if feedback=='':
        print('Enter the feedback:')
        feedback=input()
    else:
        print('Thank you for providing feedback')
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("UPDATE room_booking SET feedback=%s WHERE room_no=%s",(feedback,room_no))
    con.commit()
    cursor.close()
    con.close()
elif choice==5:
    print('Enter the room number:')
    room_no=int(input())
    con=sqlcon.connect(host="localhost",user="root",passwd="12345",database='',auth_plugin="mysql_native_password")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM room_booking WHERE room_no=%s",(room_no))
    result=cursor.fetchall()
    for row in result:
        print('Room Number:',row[0])
        print('Name:',row[1])
        print('Age:',row[2])
        print('Gender:',row[3])
        print('Email:',row[4])
        print('Phone:',row[5])
        print('Address:',row[6])
        print('Room Type:',row[7])
        print('Price:',row[8])
        print('Check In:',row[9])
        print('Check Out:',row[10])
        print('Bill:',row[11])
        print('Feedback:',row[12])
    cursor.close()
    con.close()
elif choice==6:
    print('Thank you for using Swaraj Hotel')
    exit()
else:       
'''
