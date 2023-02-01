
import os

from enum import Enum
import importlib

class Human():
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

class People(Enum):
    Alex = Human('Alex', True)
    Annabel = Human("Annabel", True)
    Elliott = Human("Elliott", False)
    Euthyme = Human('Euthyme', True)
    Gabby = Human('Gabby', True)
    George = Human("George", False)
    Jamie = Human("Jamie", False)
    Jegor = Human('Jegor', True)
    Joel = Human('Joel', True)
    Joey = Human('Joey', True)
    John = Human('John', True)
    Jonny = Human('Jonny', True)
    Josh = Human('Josh', True)
    Lewis = Human('Lewis', True)
    Luke = Human('Luke', True)
    Mark = Human('Mark', True)
    Matt = Human("Matt", False)
    Matthew = Human('Matthew', True)
    Ross = Human('Ross', True)
    Rupert = Human("Rupert", False)
    SamO = Human('SamO', True)
    SamP = Human('SamP', True)
    Sophie = Human("Sophie", False)
    TomC = Human('TomC', True)

class Utils():
    def __init__(self):
        pass

    def is_person_alive(self, name):
        is_alive = False
        for p in self.utils:
            if p.value.name == name and p.value.is_alive:
                return True
        return False

    def get_utils(self):
        return [p for p in People]

    def get_all_alive_people(self):
        return [p for p in People if p.value.is_alive]

    def get_all_votes(self):
        voting_files = [f for f in os.listdir() if f.startswith('day')]
        for f in voting_files:
            filename = f[:-3]
            print('file', filename)
            votes_for_day = importlib.import_module(filename).votes
            