#Exceptions
#Bad things happen, we need to know how to handle them




from typing import Type, final


def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner


#Try, Except and Finally
@outline
def test_one(x, y):
    try:
        z = x / y
        print(f'Result: {z}')
    except:
        #catch
        print(f'Something bad happened x: {x}, y:{y}')
    finally:
        print('Complete')


test_one(5, 0)
test_one(5, 'Cat')
test_one(5, 2)

@outline
def test_two(x, y):
    try:
       assert(x > 0)
       assert(y > 0)
    except AssertionError:
        print(f'Failed to assert x:{x}, y:{y}')
    except Exception as e:
        print(f'Something bad happened x: {x}, y:{y}, issue: {e}')
    else:
        z = x / y
        print(f'Result: {z}')
    finally:
        print('Complete')

test_two(5, 0)
test_two(5, 'Cat')
test_two(5, 2)

#User define exceptions and raising
class CatError(RuntimeError):
    def __init__(self, *args: object) -> None:
        self.args = args

@outline
def test_cats(qty):
    try:
      if not isinstance(qty, int):
          raise TypeError('Must be an int')
      if qty < 9:
          raise CatError('Must own more than 9 cats')
    except Exception as e:
      print(f'Oops: {e.args}')
    finally:
      print('Complete')

test_cats(3)
test_cats(12.3)
test_cats(11)