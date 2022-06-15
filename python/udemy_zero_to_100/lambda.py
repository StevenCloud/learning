#Squaring
numbers = [1, 5, 10, 11, 12]
print(list(map(lambda item: item*item, numbers)))

#Sorting
list_of_tuples = [(1, 5), (9,9), (8, 2), (11, 1), (6, 5)]
list_of_tuples.sort(key = lambda x: x[1])
print(list_of_tuples)
