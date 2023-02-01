from itertools import combinations

from utils import Utils

utils = Utils()


def get_all_combinations(group_size):
    all_alive_people = utils.get_all_alive_people()
    all_combinations_of_size = list(combinations(all_alive_people, group_size)) # all combinations of certain size
    return all_combinations_of_size

def get_combinations_of_groups_that_never_voted_each_other(group_size):
    all_combinations = get_all_combinations(group_size)
    votes = utils.get_votes_per_person()
    actual_combinations = []

    for combination in all_combinations:
        is_valid_combination = True
        people_in_combination = [f.value.name for f in combination]
        for person in people_in_combination:
            if any(person in people_in_combination for person in votes[person]):
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


def print_info():
    print('-----------------------------------------------------------------------------------------------------------------')
    for group_size in range(2, 8):
        groups_of_size = get_combinations_of_groups_that_never_voted_each_other(group_size)
        print(f"There are {len(groups_of_size)} possible groups of {group_size} that never voted for each other")

    print('-----------------------------------------------------------------------------------------------------------------')
    voting_for_faithful = get_number_of_times_each_person_voted_for_a_faithful_that_have_been_voted_out()
    for person in range(0, 5):
        print(f"{voting_for_faithful[person][0]} is in the top 5 for voting {voting_for_faithful[person][1]} faithfuls out")
    print('-----------------------------------------------------------------------------------------------------------------')

print_info()