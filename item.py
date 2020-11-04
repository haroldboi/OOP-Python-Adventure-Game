
class Item():
    def __init__(self,name,typez):
        self._name = name
        self._desc = None
        self._type = typez
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,namez):
        self._name = namez
    @property
    def desc(self):
        return self._desc
    @desc.setter
    def desc(self,description):
        self._desc = description
    @property
    def typei(self):
        return self._type
    @typei.setter
    def typei(self,typez):
        self._type = typez
    def describe(self):
        print (self._name+": "+self._desc)
    
    
    
