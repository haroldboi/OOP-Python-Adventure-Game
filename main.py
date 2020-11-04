from room import Room
from item import Item
from character import Character , Enemy , Friend
from rpginfo import RPGinfo
# no underscore = public
# self.my_attribute = None

# single underscore = protected
# self._my_attribute = None

# double underscore = private
# self.__my_attribute = None



#Static and class methods belongs to a class, whereas an instance methods belongs to the object.


spooksville = RPGinfo("Monster Mash")
spooksville.welcome()
RPGinfo.info()

RPGinfo.author = "Raspberry Pi Foundation"


print("-----------------------------------------------------------")
print("Commands that can be used:\nsouth , east , west , north , \ntake , hug , fight , inventory , use")
kitchen = Room("Kitchen")#Setting the self.room_name as Kitchen for the kitchen object
ballroom = Room("Ballroom")
dining_hall = Room("Dinning Hall")

kitchen.desc=("A bright marble floored modern day kitchen , with metal pans lining the walls")
                
ballroom.desc=("A dimly lit , large ballroom with massive a chandelier looming above") 
dining_hall.desc=("A large table absorbs the dining room , with large banners and pictures surronding the room") 
#Linking rooms
kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")
current_room = kitchen
#Defining Items
bag = []
acid = Item("Acid","Weapon")
key = Item("Rusty Key","Quest")
potion = Item("Red Potion","Health")
acid._desc = "A toxic green acid that is breaking through its container slightly"
key._desc = 'A old rust covered gate key '
potion._desc = "A blood red solution in a large flask with a cork screw sealing it in "
#Setting Characters to rooms
roomy  =Friend("Roomy","A short living mushroom with bright red cheeks")
roomy.set_conversation("Hi there seen any other fungi around...")
skeletor=Enemy('Skeletor',"A tall slender skeleton with a battle axe and shield ")
skeletor.set_conversation("Greetings... A humannnn , I can't believe it mmm...")                      
skeletor.set_weakness("Acid")
dining_hall._character = skeletor
ballroom._character= roomy
roomy.set_item(acid)

#setting items to rooms
kitchen._item = potion
dining_hall._item = key
game = 1 
print("There are " + str(Room.rooms) + " rooms to explore.")
while game >= 1:		
    print("\n")
    current_room.print_name()
    current_room.print_desc()
    current_room.get_details()
    item =current_room._item
    inhabitant = current_room._character
    if inhabitant is not None :
        inhabitant.describe()
    if item is not None :
        print("There is an item")
        item.describe()
    command = input("> ")
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("No one is here silly")
    elif command == 'fight':
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.fight()
            else:
                w = input("Enter what you want to fight with\n:")
                if w in bag or w == 'fist':
                    f = inhabitant.fight(w)
                    if f == True:
                        bag.remove(w)
                        dining_hall._character = None
                        print("As the bones fall you see a large gate appear on the wall with a rusty key hole")
                    elif f == False :
                        game = game - 1
                        if game <= 0:
                            print("You have been defeated and the adventutre will end here")
                            RPGinfo.credits(spooksville.title)
                        else:
                            print("The monster defeated you but you had a extra life")
                            

                    
                        
                else:
                    print("You do not have this item")
                
        else:
            print("There is no one here to fight")
    
    elif command == 'hug':
        if inhabitant is not None and isinstance(inhabitant, Friend):
            if inhabitant.item is not None:
                it = inhabitant.hug()
                bag.append(it._name)
                print(str(it._name)+" Has been added to your bag")
                print(bag)
                inhabitant.item = None
            else:
                print("["+inhabitant.name+" says]: Thats too much now")
        elif inhabitant is not None:
            print(inhabitant.name+" doesn't want to hug you , shame")
        else:
            print("There is no one to hug *cries inside*")
            
    
    elif command == 'take':
        if item is not None and len(bag)<= 10:
            bag.append(item._name)
            space = 10 - len(bag)
            print("Item taken \nSpace left: "+str(space))
            current_room._item = None
        else:
            print("No items to take")
    elif command == 'inventory':
        if len(bag) == 0:
            print("--Empty--")
        else:    
            print(bag)
            space = 10- len(bag)
            print("This much space left: "+str(space))
        
    elif command == 'use':
        if len(bag) != 0:
            print(bag)
            i = str(input("Please enter the item to use as its dispalyed in your bag\n:"))
            if i in bag:
                if i== 'Rusty Key' and dining_hall._character is None:
                    print("You use the rusty key to open the large gate ,\nYou are free")
                    RPGinfo.credits(spooksville.title)
                    game  = 0
                if i == 'Red Potion':
                    game = game + 1
                    print("You feel a strange feeling almost like you have gained a extra life")
                    bag.remove(i)
                if i == 'Acid':
                    print("You pour the acid on yourself\nNext time try using it in battle instead")
                    bag.remove(i)
                    game  = game -1 
                    if game == 0:
                        print("You have been defeated and the adventutre will end here")
                        RPGinfo.credits(spooksville.title)
                    else:
                        print("You had a extra life and remain alive")
            else:
                print(i+" Is not in your bag")

        else:
            print("You have no items")
   
                
                
            
