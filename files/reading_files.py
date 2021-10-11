#Reading a text file

# Get a filename

import os, sys

print(f'File: {__file__}')
print(f'Args: {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Reading: {sfile}')

#Exists

if not os.path.exists(sfile):
    print('File not found')
    exit(1)

# Open the file
f = open(sfile, 'r')

#Read a line
line = f.readline()
print(line)


chars = f.read(10)
print(f'Chars: *{chars}*')

#Position
print(f'Position: {f.tell()} of {os.stat(sfile).st_size}')

# Seek - move to a position in the file
#Zero based
f.seek(0)
print('--------------------------------')

for l in f.readlines():
    print(l.strip())

#Close the file
#Allows other applications to work with it
f.close()