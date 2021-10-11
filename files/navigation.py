


# Import a module
import os 


d = os.getcwd()
# print(f'Current: {d}')

# Change folders

os.chdir('..')
# print(f'Current: {os.getcwd()}')
os.chdir(d)
# print(f'Current: {os.getcwd()}')


# ListDir

for f in os.listdir():
    if os.path.isdir(f): print(f'Dir: {f}')
    if os.path.isfile(f): print(f'File: {f}')
    if os.path.islink(f): print(f'Link: {f}' )


# ScanDir

for e in os.scandir():
    print(f'Name: {e.name}')
    print(f'Path: {e.path}')



# Glob
#Recursive Scan


import glob
os.chdir('..')
dir = os.getcwd()


for filename in glob.glob(pathname= dir + "**/**", recursive=True):
    print(f'glob: {filename}')


for currentpath, folders, files in os.walk('..'):
    for file in files:
        print(f'Walk: {os.path.join(currentpath, file)}')