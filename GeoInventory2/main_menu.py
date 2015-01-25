import psycopg2
import newcatalog
import sys

# creates connection to the database
conn = psycopg2.connect("host = 168.30.240.96 dbname = three user= three password = g3")
# creates the cursor
cur = conn.cursor()

# drops table if exists, for testing only, remove for final product.
cur.execute('DROP TABLE IF EXISTS geo_inv')

cur.execute('DROP TABLE IF EXISTS users')

# creates tables
cur.execute('CREATE TABLE users (u_name varchar(80), totaluse INTERVAL);')

cur.execute('CREATE TABLE geo_inv (name varchar(80), i_type varchar(80), status varchar(10), p_num bigint,'
            'email varchar(80), tut INTERVAL, c_out TIMESTAMP, c_in TIMESTAMP);')

# saves changes
conn.commit()

# closes the cursor and the connection
cur.close()
conn.close()


class Menu:
    """Displays the menu for the GIS Inventory Database."""
    def __init__(self):
        self.catalog_functions = newcatalog.Catalog_functions()
        self.choices = {
                "1": self.catalog_functions.add_item,
                "2": self.catalog_functions.remove_item,
                "3": self.catalog_functions.update_item_name,
                "4": self.catalog_functions.update_item_type,
                "5": self.catalog_functions.update_item_email,
                "6": self.catalog_functions.update_item_phone,
                "7": self.catalog_functions.check_out,
                "8": self.catalog_functions.check_in,
                "9": self.catalog_functions.inv_reports,
                "10": self.catalog_functions.use_report,
                "11": self.catalog_functions.total_use,
                "12": self.quit
                }

    def display_menu(self):
        print("""
GIS Department Inventory

1. Add new item to the database
2. Remove item from the database
3. Update an item's name
4. Update an item's type
5. Update email
6. Update phone number
7. Check out item
8. Check in item
9. General Inventory Report
10. Usage Report
11. Total Usage Report
12. Quit
""")

    def run(self):
        """Display the current menu and respond to designated choices."""
        while True:
            self.display_menu()
            choice = raw_input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("Thank you for using your GIS Department Inventory, Goodbye.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
