


class Person:
    #Weak Private
    _name = 'No Name'
    def setName(self, name):
      self._name = name
      print(f'Name set to {self._name}')

    #Strong private
    def __think(self):
        print('Thinking to my self')
    
    def work(self):
      self.__think()

    def __init__(self):
        print('Constructor')

    def __call__(self):
        print('Call Someone ')

class Child(Person):
    def testDouble(self):
        self.__think(self)