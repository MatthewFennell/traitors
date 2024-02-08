
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

    Annabel = Human("Annabel")
    Ben = Human("Ben")
    Elliott = Human("Elliott", role=Role.FAITHFUL, demise=Demise.VOTED)
    Euthyme = Human("Euthyme")
    Gabby = Human("Gabby")
    Gary = Human("Gary", role=Role.FAITHFUL, demise=Demise.VOTED)
    Gazell = Human("Gazell")
    James = Human("James")
    Jegor = Human("Jegor")
    Jess = Human("Jess")
    Jesse = Human("Jesse")
    Joel = Human("Joel")
    Joey = Human("Joey")
    Julian = Human("Julian", role=Role.FAITHFUL, demise=Demise.VOTED)
    Kay = Human("Kay")
    Katie = Human("Katie")
    Lewis = Human("Lewis")
    Mark = Human("Mark")
    Matt = Human("Matt", role=Role.FAITHFUL)
    Molly = Human("Molly")
    Nic = Human("Nic")
    Phoebe = Human("Phoebe")
    Sam = Human("Sam")
    Samantha = Human("Samantha")
    Sophie = Human("Sophie")
    Will = Human("Will")

class Utils():
    def __init__(self):
        pass

    def get_all_people(self):
        return [p for p in People]

    def get_all_alive_people(self):
        return [p for p in People if p.value.demise == Demise.ALIVE]

    def get_all_people_or_traitors(self):
        return [p for p in People if p.value.role == Role.TRAITOR or p.value.demise == Demise.ALIVE]

    def get_all_traitors(self):
        return [p for p in People if p.value.role == Role.TRAITOR]

    def get_votes_for_all_days_in_order(self):
        voting_files = [f for f in os.listdir() if f.startswith('day')]
        all_votes = [importlib.import_module(filename[:-3]).votes for filename in voting_files]
        return all_votes

    def get_person_by_name(self, name):
        return People[name]

    def get_is_person_alive_by_name(self, name):
        person = self.get_person_by_name(name)
        return person.value.demise == Demise.ALIVE

    def get_is_person_faithful_and_voted_out_by_name(self, name):
        return People[name].value.role == Role.FAITHFUL and People[name].value.demise == Demise.VOTED

    def get_votes_per_person(self, alive_people=True):
        votes_per_person = {p.value.name: [] for p in People}
        votes_by_day = self.get_votes_for_all_days_in_order()
        for votes in votes_by_day:
            for key, value in votes.items():
                votes_per_person[key].append(value.value.name)
        return votes_per_person
            
    