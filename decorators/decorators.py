


# def test_decorator(func):
#     print('Before')
#     func()
#     print('After')


# @test_decorator
# def do_stuff():
#     print('Doing Stuff')


#Real decorator

def makeBold(func):
    def inner():
      print('<b>')
      func()
      print('</b>')
    return inner

@makeBold
def printName():
    print('Santi Racca')

printName()

#Decorators with params

def numCheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Cannot divide by zero')
                return False
            return True
        print(f'{o} is not a number')
        return False
    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)
    return inner

@numCheck
def divide(a,b):
    print(a / b)


#Decorator with unknown number of params


def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        func(*args, **args)
        print('-'*20)
    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'Args = {args}')
        print(f'args = {kwargs}')
        for x in args:
            print(f'arg = {x}')
        for k,v in kwargs.items():
            print(f'key={k}, value={v}')
    return inner

@outline
@list_items
def display(msg):
    print(msg)

display('Hello World')

@outline
@list_items
def birthday(name="", age=0):
    print(f'Happy Birthday {name} you are {age} years old')