from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capital(item):
    return item.capitalize()

print(list(map(capital, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()

print(list(zip(my_numbers, my_strings)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def pass_score(item):
    return item > 50

print(list(filter(pass_score, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate(curr_val, new_val):
    return curr_val + new_val

print(reduce(accumulate, my_numbers) + reduce(accumulate, scores))
