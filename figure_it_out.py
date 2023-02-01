from itertools import combinations

from utils import Utils

utils = Utils()


def get_all_combinations():
    all_alive_people = utils.get_all_alive_people()
    all_combinations_of_three = list(combinations(all_alive_people, 3))
    return all_combinations_of_three


utils.get_all_votes()