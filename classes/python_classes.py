


from cat import Cat

def test():
    a = Cat("Gordo", 1, 'tabby')
    b = Cat("Wanda", 6, 'black')
    print(a)
    print(b)
    b.describe()
    a.describe()

    a.meow()
    b.sleep()
    a.hungry()
    a.eat()

if __name__ == "__main__":
    x = Cat('Test')
    print(x)
    test()


