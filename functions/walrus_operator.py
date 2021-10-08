


# y := len('Hello')
(y := len('hello'))
print(y)

people = ['Santi', 'Lara', 'tony']
if n := len(people) <= 3: print(n)


#Simple Example

lines = []

def canAdd(max = 5):
    global lines
    if allowed := (count := len(lines)) < max:
      print(f'You can enter {max - count} more')
    return allowed

while canAdd():
  lines.append(l := input('Enter a line: '))

print(f'You entered: {lines}')