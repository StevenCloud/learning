#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('cat1', 5)
cat2 = Cat('cat2', 10)
cat3 = Cat('cat3', 15)


# 2 Create a function that finds the oldest cat
def find_oldest():
    oldest_cat = max(cat1.age, cat2.age, cat3.age)
    return oldest_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {find_oldest()} years old.")