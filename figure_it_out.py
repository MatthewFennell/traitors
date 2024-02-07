from itertools import combinations

from utils import Utils

utils = Utils()


def get_all_combinations(group_size):
    all_people = utils.get_all_people_or_traitors()
    all_combinations_of_size = list(combinations(all_people, group_size)) # all combinations of certain size
    return all_combinations_of_size

def get_combinations_of_groups_that_never_voted_each_other(group_size):
    all_combinations = get_all_combinations(group_size)
    votes = utils.get_votes_per_person()
    actual_combinations = []

    all_traitors = utils.get_all_traitors()

    for combination in all_combinations:
        is_valid_combination = True
        people_in_combination = [f.value.name for f in combination]
        for person in people_in_combination:
            if any(person in people_in_combination for person in votes[person]):
                is_valid_combination = False
                break

        for traitor in all_traitors:
            if traitor.name not in people_in_combination:
                is_valid_combination = False
                break        
        if is_valid_combination:
            actual_combinations.append(combination)
    return actual_combinations

def get_number_of_times_each_person_voted_for_a_faithful_that_have_been_voted_out():
    votes = utils.get_votes_per_person()
    all_alive_people = utils.get_all_alive_people()
    votes_on_faithful = {p.value.name: 0 for p in all_alive_people}
    for key, val in votes.items():
        if not utils.get_is_person_alive_by_name(key):
            continue
        count = 0
        for person_name in val:
            is_faithful = utils.get_is_person_faithful_and_voted_out_by_name(person_name)
            if is_faithful:
                count += 1
        votes_on_faithful[key] = count

    votes_list = []
    for x,y in votes_on_faithful.items():
        votes_list.append((x,y))
    votes_list = sorted(votes_list, key=lambda x: x[1], reverse=True)

    return votes_list

def find_people_traitors_never_voted_for():
    traitors = utils.get_all_traitors()
    votes_per_person = utils.get_votes_per_person()
    set_of_people_traitors_voted = {}
    for traitor in traitors:
        set_of_people_traitors_voted = {*votes_per_person[traitor.name], *set_of_people_traitors_voted}
    alive_people = utils.get_all_alive_people()
    alive_people_not_voted_by_known_traitor = []
    for person in alive_people:
        if person.name not in set_of_people_traitors_voted:
            alive_people_not_voted_by_known_traitor.append(person.name)
    return alive_people_not_voted_by_known_traitor


def print_info():
    print('-----------------------------------------------------------------------------------------------------------------')
    for group_size in range(2, 5):
        groups_of_size = get_combinations_of_groups_that_never_voted_each_other(group_size)
        print(f"There are {len(groups_of_size)} possible groups of {group_size} that never voted for each other")
        for x in groups_of_size:
            a = ""
            for y in x:
                a += y.name + ","
            print(a)

    print('-----------------------------------------------------------------------------------------------------------------')
    voting_for_faithful = get_number_of_times_each_person_voted_for_a_faithful_that_have_been_voted_out()
    for person in range(0, 5):
        print(f"{voting_for_faithful[person][0]} is in the top 5 for voting {voting_for_faithful[person][1]} faithfuls out")
    print('-----------------------------------------------------------------------------------------------------------------')

    not_voted_by_traitors = find_people_traitors_never_voted_for()
    print("People not voted by traitors", not_voted_by_traitors)

print_info()