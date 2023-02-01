
import os

from enum import Enum
import importlib

class Role(Enum):
    FAITHFUL = "FAITHFUL"
    TRAITOR = "TRAITOR"
    UNKNOWN = "UNKNOWN"

class Demise(Enum):
    VOTED = "VOTED"
    KILLED = "KILLED"
    ALIVE = "ALIVE"

class Human():
    def __init__(self, name, role=Role.UNKNOWN, demise=Demise.ALIVE):
        self.name = name
        self.role = role
        self.demise = demise

class People(Enum):
    Alex = Human('Alex')
    Annabel = Human("Annabel")
    Elliott = Human("Elliott", role=Role.FAITHFUL, demise=Demise.VOTED)
    Euthyme = Human('Euthyme')
    Gabby = Human('Gabby')
    George = Human("George", role=Role.FAITHFUL, demise=Demise.KILLED)
    Jamie = Human("Jamie", role=Role.FAITHFUL, demise=Demise.VOTED)
    Jegor = Human('Jegor')
    Joel = Human('Joel')
    Joey = Human('Joey')
    John = Human('John')
    Jonny = Human('Jonny')
    Josh = Human('Josh')
    Lewis = Human('Lewis')
    Luke = Human('Luke')
    Mark = Human('Mark')
    Matt = Human("Matt")
    Matthew = Human('Matthew', role=Role.FAITHFUL, demise=Demise.KILLED)
    Ross = Human('Ross')
    Rupert = Human("Rupert", role=Role.FAITHFUL, demise=Demise.VOTED)
    SamO = Human('SamO')
    SamP = Human('SamP')
    Sophie = Human("Sophie", role=Role.FAITHFUL, demise=Demise.KILLED)
    TomC = Human('TomC')

class Utils():
    def __init__(self):
        pass

    def get_utils(self):
        return [p for p in People]

    def get_all_alive_people(self):
        return [p for p in People if p.value.demise == Demise.ALIVE]

    def get_votes_for_all_days_in_order(self):
        voting_files = [f for f in os.listdir() if f.startswith('day')]
        all_votes = [importlib.import_module(filename[:-3]).votes for filename in voting_files]
        return all_votes

    def get_person_by_name(self, name):
        return People[name]

    def get_is_person_faithful_and_voted_out_by_name(self, name):
        return People[name].value.role == Role.FAITHFUL and People[name].value.demise == Demise.VOTED

    def get_votes_per_person(self):
        votes_per_person = {p.value.name: [] for p in People}
        votes_by_day = self.get_votes_for_all_days_in_order()
        for votes in votes_by_day:
            for key, value in votes.items():
                votes_per_person[key].append(value.value.name)
        return votes_per_person
            
    