import psycopg2
# from tabulate import tabulate


class Catalog_functions():

    def __init__(self):
        self.conn = psycopg2.connect(dbname='three', user='three', host='168.30.240.96', password='g3')
        self.cur = self.conn.cursor()

    def add_item(self):
        """Adds an item to the database based on user input."""
        self.name = raw_input("What is the name of the item? ")
        self.i_type = raw_input("What is the type of the item? ")
        self.cur.execute("""INSERT INTO geo_inv VALUES(%s,%s,'In', 0, 'None', null, null, null);""", (self.name, self.i_type,))
        self.conn.commit()
        print ('Item successfully added to the database.')

    def remove_item(self):
        """Deletes an item from the database based on user input."""
        self.name = raw_input("What is the name of the item you wish to delete? ")
        self.cur.execute("""DELETE FROM geo_inv WHERE name =%s;""", (self.name,))
        self.conn.commit()
        print ('Item successfully deleted from the database.')

    def update_item_name(self):
        """Updates an item's name in the database based on user input."""
        self.name = raw_input("What is the name of the item you wish to update? ")
        self.new_name = raw_input("What is the new name you wish to give the item? ")
        self.cur.execute("""UPDATE geo_inv SET name =%s WHERE name =%s;""", (self.new_name, self.name,))
        self.conn.commit()
        print ('Item name successfully updated in the database.')

    def update_item_type(self):
        """Updates an item's type in the database based on user input."""
        self.name = raw_input("What is the name of the item you wish to update? ")
        self.i_type = raw_input("What is the new type you wish to give this item? ")
        self.cur.execute("""UPDATE geo_inv SET i_type =%s WHERE name =%s;""", (self.i_type, self.name,))
        self.conn.commit()
        print ('Item type successfully updated in the database.')

    def update_item_email(self):
        """Updates an item's email reference in the database based on user input."""
        self.name = raw_input("What is the name of the item you wish to update? ")
        self.new_email = raw_input("What is the new email you wish to attach to this item? ")
        self.cur.execute("""UPDATE geo_inv SET email = %s WHERE name = %s;""", (self.new_email, self.name,))
        self.conn.commit()
        print ('Item email reference successfully updated in the database.')

    def update_item_phone(self):
        """Updates an item's phone number reference in the database based on user input."""
        self.name = raw_input("What is the name of the item you wish to update? ")
        self.new_num = raw_input("What is the new phone number you wish to attach to this item? ")
        self.cur.execute("""UPDATE geo_inv SET p_num = %s WHERE name = %s;""", (self.new_num, self.name,))
        self.conn.commit()
        print ('Item phone number reference successfully updated in the database.')

    def inv_reports(self):
        """Selects all items currently in the database and exports them to a csv file on users desktop."""
        self.cur.execute("""SELECT * FROM geo_inv;""")
        rows = self.cur.fetchall()
        f = open("C:/Users/crswin5726/Desktop/output.csv", "w")
        f.write("Name, Inventory Type, Status, Phone Number, Email, Total Uses Time, Check Out Time, Check In Time")
        f.write('\n')
        for row in rows:
            str_row = [str(item) for item in row]
            f.write(",".join(str_row))
            f.write('\n')
        f.close()
        print ('Check your Desktop for an Inventory Report in csv format.')

    def use_report(self):
        """Selects and exports the total number of users and total usage time."""
        self.cur.execute("""SELECT COUNT(u_name), SUM(totaluse) FROM users;""")
        rows = self.cur.fetchall()
        f = open("C:/Users/crswin5726/Desktop/simpleuse.csv", "w")
        f.write("Total Users, Total Usage Time")
        f.write('\n')
        for row in rows:
            str_row = [str(item) for item in row]
            f.write(",".join(str_row))
            f.write('\n')
        f.close()
        print ('Check your Desktop for a simplified Use Report in csv format.')

    def total_use(self):
        """Selects and exports unique users and total time used report to a csv file."""
        self.cur.execute("""SELECT SUM(totaluse), u_name FROM users GROUP BY u_name;""")
        rowss = self.cur.fetchall()
        e = open("C:/Users/crswin5726/Desktop/totaluse.csv", "w")
        e.write("Total Usage Time, User Name")
        e.write('\n')
        for row in rowss:
            str_rows = [str(item) for item in row]
            e.write(",".join(str_rows))
            e.write('\n')
        e.close()
        print ('Check your Desktop for a Total Usage Report in csv format.')

    def check_out(self):
        """This checks out an item from the database and updates columns."""
        self.name = raw_input("What is the name of the item you wish to check out? ")
        self.e_mail = raw_input("What is your email? ")
        self.p_num = raw_input("What is your phone number? ")
        self.u_name = raw_input("What is your name? ")
        self.cur.execute("""UPDATE geo_inv SET email =%s WHERE name =%s;""", (self.e_mail, self.name,))
        self.cur.execute("""UPDATE geo_inv SET p_num =%s WHERE name =%s;""", (self.p_num, self.name,))
        self.cur.execute("""UPDATE geo_inv SET c_out = NOW() WHERE name =%s;""", (self.name,))
        self.cur.execute("""UPDATE geo_inv SET status = 'Out' WHERE name =%s;""", (self.name,))
        self.cur.execute("""INSERT INTO users VALUES (%s, null);""", (self.u_name,))
        self.conn.commit()
        print ('Item successfully checked out from inventory.')

    def check_in(self):
        """This checks in an item to the database and updates appropriate columns."""
        self.u_name = raw_input("What is your name? ")
        self.name = raw_input("What is the name of the item you wish to check in? ")
        self.cur.execute("""UPDATE geo_inv SET status = 'In' WHERE name =%s;""", (self.name,))
        self.cur.execute("""UPDATE geo_inv SET c_in = NOW() WHERE name =%s;""", (self.name,))
        self.conn.commit()
        self.cur.execute("""UPDATE geo_inv SET tut = (c_in - c_out) WHERE name =%s;""", (self.name,))
        self.conn.commit()
        self.cur.execute("""UPDATE users SET totaluse = (SELECT tut FROM geo_inv WHERE name =%s) WHERE u_name=%s;""", (self.name, self.u_name))
        self.conn.commit()
        print ('Item successfully checked in to inventory.')
