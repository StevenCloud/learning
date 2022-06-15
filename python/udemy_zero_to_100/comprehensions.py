#Comprehension duplicates

test = [1, 1, 2, 3]
duplicates = [num for num in test if test.count(num) > 1]
print(list(set(duplicates)))
