



#Import as
import mycode as person

#Scope issues

global name


print(person.name)

#Test the code
person.name = 'Santi'

person.greet()

person.toFile('test.txt')

person.name = 'Tammy'

person.greet()

person.fromFile('test.txt')
person.greet()