"""Basic Module"""
from pymongo import MongoClient

def confirm(prompt=None, resp=False):
    """Confirmation Prompt"""
    if prompt is None:
        prompt = 'Confirm'
    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')

    while True:
        ans = input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print('please enter y or n.')
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False

def setplayerdetails():
    """Request input for user details"""
    tempdetails = {}
    while True:
        try:
            name = str(input("Enter Name: "))
        except ValueError:
            print("Not a string!")
            continue
        else:
            tempdetails["Name"] = name
            break

    while True:
        try:
            quality = int(input("Enter Quality: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            tempdetails["quality"] = quality
            break

    while True:
        try:
            combat = int(input("Enter Combat: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            tempdetails["combat"] = combat
            break
    return tempdetails

class Database:
    """Main Database Class"""
    _id = 0
    def __init__(self, uri, data, collection):
        """Set up data class"""
        self.myuri = MongoClient(uri)
        self.mydata = self.myuri[data]
        self.localdata = self.mydata[collection]
        # self.localdata = self.mydata.self.mycollection
    def clear(self):
        """Clears data Warband"""
        result = self.localdata.delete_many({})
        print("Cleared Warband of: %d entries" % (result.deleted_count))
    def check_add(self, player):
        """Add player to database"""
        result = self.localdata.insert_one(player)
        print(self.localdata.collection_names(include_system_collections=False))
        print(self.localdata.find())
    def get(self, _id):
        """Function to get record from data:"""
        document = self.localdata.find_one({'_id': _id})
        print(document)
    def listall(self):
        """Function to get all records from data:"""
        documentlist = self.localdata.find({})
        print(documentlist)

def main():
    """Main Menu Area"""
    choice = '0'
    activedatabase = Database("mongodb://localhost:27017", "asobhdata", "asobhtable")
    while choice == '0':
        print("MENU")
        print("4. data - Add Figure to Warband")
        print("5. data - Show Warband")
        print("6. data - Clear Warband")
        print("9. exit")
        choice = input("Please make a choice: ")
    if choice == "9":
        quit()
    elif choice == "6":
        print("data clear")
        activedatabase = activedatabase.clear
    elif choice == "5":
        activedatabase = activedatabase.listall
    elif choice == "4":
        print("data add")
        newplayeradd = {}
        newplayeradd = setplayerdetails()
        for keys,values in newplayeradd.items():
            print(keys)
            print(values)
        
        # activedatabase = activedatabase.check_add(newplayeradd)
    else:
        print("I don't understand your choice.")

## Main menu! Commented to test Mongo
while True:
    main()
