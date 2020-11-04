class RPGinfo():
    author = 'BigBoi'
    def __init__(self,name):
        self.title = name
    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
         print("Made using my amazing powers and Raseberry Pi's awesome team")

    @classmethod
    def credits(cls,name):
         print("Thanks for playing "+str(name))
         print("Created by "+cls.author)
