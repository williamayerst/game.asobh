"""Basic Module"""
from pymongo import MongoClient
from bson import ObjectId

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
            tempdetails["name"] = name
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
    def clear(self):
        """Clears data Warband"""
        result = self.localdata.delete_many({})
        print("Cleared Warband of: %d entries" % (result.deleted_count))
    def check_add(self, player):
        """Add player to database"""
        self.player = player
        result = self.localdata.insert_one(self.player).inserted_id
        print('Added player as ID {id}.'.format(id=result))
    def get(self, player_id):
        """Function to get record from data:"""
        document = self.localdata.find_one({"_id":ObjectId(player_id)})
        print(document)
    def listall(self):
        """Function to get all records from data:"""
        documentlist = self.localdata.find()
        for document in documentlist:
            print(document)

def main():
    """Main Menu Area"""
    choice = '0'
    activedatabase = Database("mongodb://localhost:27017", "asobhdata", "asobhtable")
    while choice == '0':
        print("MENU")
        print("1. Add Figure to Warband")
        print("2. Show Warband")
        print("3. Clear Warband")
        print("4. Get specific player")
        print("9. exit")
        choice = input("Please make a choice: ")
    if choice == "9":
        quit()
    elif choice == "4":
        player_id = str(input("Enter ID: "))
        activedatabase.get(player_id)
    elif choice == "3":
        activedatabase.clear()
    elif choice == "2":
        activedatabase.listall()
    elif choice == "1":
        newplayeradd = {}
        newplayeradd = setplayerdetails()
        activedatabase.check_add(newplayeradd)
    else:
        print("I don't understand your choice.")

## Main menu! Commented to test Mongo
while True:
    main()
