

import json
import os.path

class Inventory:
    pets = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: total = {self.pets[key]}')
        

    def remove(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        if q < 0:
          q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key}: total = {self.pets[key]}')
    
    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')
    
    def save(self):
      print('Saving inventory')
      with open('inventory.txt', 'w') as f:
        json.dump
      print('Saved!')

    def load(self):
        pass