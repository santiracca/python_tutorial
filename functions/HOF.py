

def test(name, age, pet):
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'pet = {pet}')

def getData():
    return dict(name="Santi", age=46, pet="Cat")

d = getData()
test(**getData())

#Function as an argument
def funky(data):
    d = data()
    print(d)

funky(getData)

