from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['asobhdb']
warband = db['asobhwarband']
localwarband = db.warband
_id = 0

post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}
localwarband.insert_one(post)
# post_id = localwarband.insert_one(post).inserted_id
print (*db.collection_names(include_system_collections=False))
print (localwarband.find())
# print (localwarband.find_one({"_id": post_id}))

# The web framework gets post_id from the URL and passes it as a string
def get(_id):
    # Convert from string to ObjectId:
    document = client.db.warband.find_one({'_id': _id})
    

def confirm(prompt=None, resp=False):
    # Confirmation Prompt
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
    # Request input for user details
    while True:
        try:
            name = str(input("Enter Name: "))
        except ValueError:
            print("Not a string!")
            continue
        else:
            break

    while True:
        try:
            quality = int(input("Enter Quality: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break

    while True:
        try:
            combat = int(input("Enter Combat: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break
    return name, quality, combat


class figure:
    """Basic figure class, with ability to return stats, etc."""
    def __init__ (self, name, quality, combat):
        """Basic figure class, with ability to return stats, etc."""
        self.name = name
        self.quality = quality
        self.combat = combat
    def stats(self):
        """Basic figure class, with ability to return stats, etc."""
        stats = {'name':self.name, 'quality':self.quality, 'combat':self.combat}
        return stats

    def add(self):
        """Basic figure class, with ability to return stats, etc."""
        global warbandlist
        print ("Adding new figure with following details: Name:%s, Quality:%d, Combat:%d to Warband - OK?" %(self.name, self.quality, self.combat))
        if confirm() == True:
            print ("Adding to list")
            warbandlist.append({'name':self.name, 'quality':self.quality, 'combat':self.combat})
        else:
            print ("Skipping")

def clearwarband():
    global localwarband
    result = db.restaurants.delete_many({})
    print("Cleared Warband of: %d entries" % (result.deleted_count))

def main():
    """Main Menu Area"""
    global warbandlist
    choice = '0'
    while choice == '0':
        print("MENU")
        print("1. Add Figure to Warband")
        print("2. Show Warband")
        print("3. Initialise Warband")
        print("4. DB - Add Figure to Warband")
        print("5. DB - Show Warband")
        print("6. DB - Clear Warband")
        print("9. exit")
        choice = input ("Please make a choice: ")
    if choice == "9":
        quit()
    elif choice == "6":
        clearwarband()
    elif choice == "5":
        print("DB show")
    elif choice == "4":
        print("DB add")
    elif choice == "3":
        warbandlist = []
    elif choice == "2":
        print(warbandlist, sep='\n')
    elif choice == "1":
        # Put user input for new player into figure class
        newplayer = figure(*setplayerdetails())
        # Add figure to warband
        newplayer.add()
    else:
        print("I don't understand your choice.")

## Main menu! Commented to test Mongo
#while True:
    #main()

# Insubstantiate new warband list


#name = str(input("Enter Name: "))
#quality = int(input("Enter Quality: "))
#combat = int(input("Enter Combat: "))


#newplayer = figure()

# Call function to populate class statistics
#newplayer.create()

# Print character object
