
#Packing Data
def pack(*nums):
    print(f'Packed: {nums}')
    for x in nums:
        print(f'Packed: {x}')

pack(1,2,3)

#Unpacking data
def unpack(a,b,c):
    print('Unpack')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

num = [1,2,3]
unpack(*num)

# Dictionary Issue

d = dict(name="Santi", age=46, pet="Cat")
print("Packing dictionary")
pack(*d)

print('Unpacking dictionary')
unpack(*d)

# Packing a Dictionary

def packdict(**nums):
    print(f'nums = {nums}')
    for k in nums:
        print(f'Packed: {k} = {nums[k]}')

packdict(name="Santi", age=46, pet="Cat")


#Unpacking a dictionary
def unpackdict(name, age, pet):
    print('Unpacking a dictionary');
    print(f'Name = {name}');
    print(f'Age = {age}');
    print(f'Pet = {pet}')

unpackdict(**d)