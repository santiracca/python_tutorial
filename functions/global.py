

x = 1
def test():
  print(x)


test()
print(x)

# Global Variable
counter = 0


# Scope Issues
def count(max):
    global counter
    counter += 1
    if counter >= max: return False
    return True

# Global keyword in action
limit = 5
for x in range(limit):
    b = count(limit)
    print(counter)