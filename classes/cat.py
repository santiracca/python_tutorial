

class Cat:
    name = ''
    age = 0
    color = ''


    def __init__(self, name, age=0, color="white"):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')
    
    def meow(self):
        print(f'{self.name} meow')

    def sleep(self):
        print(f'{self.name} zzz')

    def hungry(self):
        for x in range(5):
            self.meow()
    
    def eat(self):
        print(f'{self.name} mom mom mom')

    def describe(self):
        print(f'{self.name} is a {self.color} cat, who is {self.age} years old')
    




class Feline:
    def __init__(self, name):
      self.name = name
      print('Creating a feline')


    def meow(self):
      print(f'{self.name}: meow')

    def setName(self, name):
        print(f'{self} setting name: {name}')


class Lion(Feline):
    def roar(self):
      print(f'{self.name} roar')

class Tiger(Feline):

    
    def stalk(self):
        print(f'{self.name}: stalking')

    def rename(self, name):
        super().setName(name)



c = Feline('Kitty')
print(c)

c.meow()

l = Lion('Leo')
print(l)

l.meow()
l.roar()

t = Tiger()
print(t)
t.stalk()
t.rename('Tony')
t.meow()
t.stalk()