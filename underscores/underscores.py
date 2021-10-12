#The underscore
#Often ignored, multiple uses
#_Single
#__Double
#__Before
#After__
#__Both__


#Skipping
for _ in range(5):
    print('hello')

#Test class
from person import *

#Before (Single)
#Internal use only, called a weak private
p = Person()
p.setName('Santi')

#Before (double)

p = Person()
p.work()
# p.__think()
# c = Child()
# c.testDouble()

# After (Any)
class_ = Person()
print(class_)
