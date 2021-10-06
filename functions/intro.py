

# No Arguments
def test():
  print('Normal function')

print('\r\n----- No Arguments')
test()

#Positional and Keyword Arguments
def message(name, msg, age):
    print(f'Hello {name}, {msg}, you are {age} years old')

print('\r\n----- Positional and Keyword Arguments')
message('Santi', 'You suck', 29) #positional
message('You suck', 29, 'You suck') #positional (wrong order)
message(msg="Good Morning", name="Santi", age=29) #Keywords
message('Santi', age=29, msg="good morning")


# Internal Functions

def counter():
    def display(count = 0):
        print(f'Internal: {count}')
    for x in range(5): display(x)

    
print('\r\n----- Internal function')
counter()


# *args - positional variable length Arguments
def multiply(*args):
  z = 1
  for num in args:
      print(f'Num = {num}')
      z *= num
  print(f'Multiply: {z}')


print('\r\n----- *args')
multiply(1,2,3)
  


# **kwargs is used to pass a keyworded, variable length Arguments
def profile(**person):
    print(person)

    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    
    display('name')
    display('age')
    display('pet')

print('\r\n----- **kwargs')
profile(name="Santi", age=46, pet='Cat')

#Lambda functions (anonymous functions)
print('\r\n----- Lambda')
#Normal
def makessqft(width=0, height=0):
  return width * height
print(makessqft(width=10, height=8))
print(makessqft(15, 8))


#Lambda
#z = lambda x: x * y
sqft = lambda width=0, height=0: width * height
print(sqft(5, 5))