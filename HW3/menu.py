import sys
from notebook import Notebook, Note

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                "1": self.show_notes,
                "2": self.show_priority,
                "3": self.search_notes,
                "4": self.add_note,
                "5": self.modify_note,
                "6": self.modify_priority,
                "7": self.quit
                }

    def display_menu(self):
        print("""
Notebook Menu

1. Show all Notes
2. List Notes by Priority
3. Search Notes
4. Add Note
5. Modify Note
6. Change Priority
7. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = raw_input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}\n{3}".format(
                note.id, note.tags, note.memo, note.priority))

    def show_priority(self):
        High = self.notebook.search('High Priority')
        Low = self.notebook.search('Low Priority')
        No = self.notebook.search('No Priority')
        print (High, Low, No)

    def search_notes(self):
        filter = raw_input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = raw_input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = raw_input("Enter a note id: ")
        memo = raw_input("Enter a memo: ")
        tags = raw_input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def modify_priority(self):
        id = raw_input("Enter a note id: ")
        priority = raw_input("Enter the new priority: ")
        if priority:
            self.notebook.modify_priority(id, priority)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
