from item import Item
class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
       

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):#Sub Class of Character
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description
                         )#Call constructor from superclass to set up attributes from the main class
        self.weakness = None
    def get_weakness(self):
        return self.weakness()
    def set_weakness(self,weak_item):
        self.weakness = weak_item
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
     
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)#Call constructor from superclass to set up attributes from the main class
        self.item  = None
    def fight(self):
        print("You cannot fight "+self.name+" try offering a hug instead")
    def hug(self):
        itemz = self.item
        if self.item is not None :
            print("["+ self.name + " says]: Why thank you here is a free item:"+itemz._name)
            return self.item
            self.item = None
        else:
            print("["+ self.name + " says]:I don't want to hug ")
            return False
    def get_item(self):
        return True
    def set_item(self,i):
        self.item = i 
