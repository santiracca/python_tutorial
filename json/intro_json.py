# JSON Files

"""
{
    name: Santi
    age: 29
    pet: Cat
}
"""

# Imports
import json
filename = 'json.txt'


#To String
outD = dict(name="Santi", age=29, pet="Cat")
s = json.dumps(outD)
print(f'String={s}')


#To file
with open(filename, 'w') as f:
    json.dump(outD, f)

# From String
inD = json.loads(s)
print(f'Dictionary={inD}')


#From file
with open(filename, 'r') as f:
  fD = json.load(f)
print(f'Type: {type(fD)} = {fD}')