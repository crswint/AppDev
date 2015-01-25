import psycopg2
import random

# contributions made by Jacob Nolan
# make sure psycopg2 plugin is installed to connect to the database

# This connects to the database
conn = psycopg2.connect("host = xx.xxx.xxx.xx dbname = xxxxx user= xxx password = xx")

# Create the Cursor
cur = conn.cursor()

# Create the Table
cur.execute('DROP TABLE IF EXISTS geoinv')
# Inserts Data into the Table
cur.execute('CREATE TABLE geoinv (name varchar(80), type varchar(80), status varchar(10), serial bigint,'
            'phonenumber bigint, email varchar(80));')

cur.execute("INSERT INTO geoinv (name, type, status, serial, phonenumber, email) VALUES (%s, %s, %s, %s, %s, %s)",
            ('trimble', 'collector', 'In', 0001, 0, 'None'))

cur.execute("INSERT INTO geoinv (name, type, status, serial, phonenumber, email) VALUES (%s, %s, %s, %s, %s, %s)",
            ('trimble2', 'collector', 'Out', 0002, 4049993320, 'jpeters@gmail.com'))

cur.execute("INSERT INTO geoinv (name, type, status, serial, phonenumber, email) VALUES (%s, %s, %s, %s, %s, %s)",
            ('antenna1', 'pole antenna', 'In', 0003, 0, 'None'))

cur.execute("INSERT INTO geoinv (name, type, status, serial, phonenumber, email) VALUES (%s, %s, %s, %s, %s, %s)",
            ('antenna2', 'backpack antenna', 'Out', 0004, 4043332293, 'rsmith@gmail.com'))

cur.execute("INSERT INTO geoinv (name, type, status, serial, phonenumber, email) VALUES (%s, %s, %s, %s, %s, %s)",
            ('backpack1', 'backpack connector', 'Out', 0005, 6783329934, 'kvonn@gmail.com'))

# Make the changes to the database persistent
conn.commit()

#MENU FOR THE PROJECT (JACOB NOLAN)

reply = None

#This line ensures that if the user puts in any of these strings,
#the program will automatically close.

options = ['q', 'Q', 'quit', 'Quit', 'exit', 'Exit', 'done', 'Done']
#Initiates the while loop.

while reply not in options:
    print("""
                Welcome to the Geo Inventory Database.

              1 = Add Item to Inventory
              2 = Remove Item from Inventory
              3 = Check in Item
              4 = Check out Item
              5 = Inventory Status Report"""
        )

    reply = raw_input("Please select a option: ")

#To add the functions you must write, continue after this line with
#if statements such as
    #if reply ==str(1):
    #and so on.

# Add Item function
    if reply == str(1):
        '''Option 1 Adds an Item to Inventory '''
        serial = random.randrange(0,100000000000)
        SQL = "INSERT INTO geoinv(name, type, status, serial, phonenumber, email)VALUES(%s, %s, %s, %s, %s, %s);"
        data = ((raw_input('Type the device name. ')),)
        data1 = ((raw_input('What type of device is this? ')),)
        data2 = "In"
        data3 = serial
        data4 = 0
        data5 = "None"
        cur.execute(SQL, (data, data1, data2, data3, data4, data5))
        conn.commit()
        cur.execute("""SELECT * FROM geoinv;""")

# Remove Item function
    if reply == str(2):
        '''Option for Remove Item in Inventory'''
        cur = conn.cursor()
        Name = str(raw_input("Type the name of the device you want to remove. "))
        cur.execute("DELETE FROM geoinv WHERE name = '{0}'".format(Name))
        conn.commit()
        cur.execute("""SELECT * FROM geoinv;""")

# Check In Function
    if reply == '3':
        '''Option 3 provides the Check in Function.'''
        #Gives them the option of Serial number or Name look up
        print('If you would rather type in serial code number type None.')
        Item = str(raw_input('Please enter Item name: '))
        #If the name is not 'None' it goes through the process of using the serial number.
        if Item == 'None':
            Serial = int(raw_input('Please Enter Serial Number: '))
            cur = conn.cursor()
            cur.execute("UPDATE geoinv SET status = 'In' WHERE serial = {0}".format(Serial))
            cur.execute("UPDATE geoinv SET phonenumber = 0 WHERE serial = {0}".format(Serial))
            cur.execute("UPDATE geoinv SET email = 'None' WHERE serial = {0}".format(Serial))
        #If name is given then this goes through the process of using the name to check in the function.
        else:
            cur = conn.cursor()
            cur.execute("UPDATE geoinv SET status = 'In' WHERE name = '{0}'".format(Item))
            cur.execute("UPDATE geoinv SET phonenumber = 0 WHERE name = '{0}'".format(Item))
            cur.execute("UPDATE geoinv SET email = 'None' WHERE name = '{0}'".format(Item))
        conn.commit()
        print('Inventory Updated, Thank you!')

#Check Out Function
    if reply == '4':
        '''Option 4 preforms the Check out Function.'''
        #Gives the option of using serial number or item name look up
        print('If you would rather type in serial code number type None.')
        Item = str(raw_input('Please enter Item name: '))
        #Serial number option
        if Item == 'None':
            Serial = int(raw_input('Please Enter Serial Number: '))
            print('To check out {0} please input the following information:'.format(Serial))
            #Collects email and phone number for check out
            email = raw_input('Please input Email: ')
            phone = raw_input('Please input Phone Number: ')
            #Initiates cursor and updates rows by finding objects serial number
            cur = conn.cursor()
            cur.execute("UPDATE geoinv SET status = 'Out' WHERE serial = {0}".format(Serial))
            cur.execute("UPDATE geoinv SET phonenumber = {0} WHERE serial = {1}".format(phone, Serial))
            cur.execute("UPDATE geoinv SET email = '{0}' WHERE serial = {1}".format(email, Serial))
        #Item name option
        else:
            print('To check out {0} please input the following information:'.format(Item))
            #Collects email and phone number for check out
            email = raw_input('Please input Email: ')
            phone = raw_input('Please input Phone Number: ')
            #Initiates cursor and updates rows by finding objects name
            cur = conn.cursor()
            cur.execute("UPDATE geoinv SET status = 'Out' WHERE name = '{0}'".format(Item))
            cur.execute("UPDATE geoinv SET phonenumber = {0} WHERE name = '{1}'".format(phone, Item))
            cur.execute("UPDATE geoinv SET email = '{0}' WHERE name = '{1}'".format(email, Item))
        conn.commit()
        print('Process complete. You may go pick up your Item in the supply room.')

# Export Function
    if reply == '5':
        '''Option 5 exports the table to a csv file on the users desktop.'''
        cur.execute("SELECT * FROM geoinv")
        rows = cur.fetchall()
        # Opens a blank csv file to the filepath indicated
        f = open("C:/Users/zmiller/Desktop/output.csv", "w")
        # This populates the file
        for row in rows:
            str_row = [str(item) for item in row]
            f.write(",".join(str_row))
            f.write('\n')
        f.close()
        print('Check your Desktop for a .cvs file.')

print('Close Geo Database. Goodbye.')

# Close communication with the database
cur.close()
conn.close()
