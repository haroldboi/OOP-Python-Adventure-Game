class Room():
    rooms = 0
    def __init__(self,room_name):#Defning the class structure using the __init__ constructor
        self._name = room_name
        self.linked_rooms = {}
        self._description = None
        self._character = None
        Room.rooms = Room.rooms + 1
        self._item = None
    @property    
    def desc(self):#Will return the room description for a object
        return self._description
    @desc.setter
    def desc(self,room_description):#Whatever the room_desc is entered as it is set to that within the object
        self._description = room_description
    def print_desc(self):
        print(self._description)
    @property    
    def name(self):
        return self._name
    @name.setter
    def name(self,room_name):
        self._name = room_name
    def print_name(self):
        print(self._name)
    def describe(self):
        print(self._description)
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link
       #Printing the linked rooms associated with each room
    @property
    def characters(self):
        return self._character
    @characters.setter
    def characters(self,char_name):
        self._character = char_name
    @property
    def items(self):
        return self._item
    @items.setter
    def items(self,n_item):
        self._item = n_item
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The "+room._name + " is " +direction)
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
