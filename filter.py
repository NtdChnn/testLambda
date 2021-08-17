def even(a):
    if a % 2 == 0:
        return a


thisList = [1, 2, 3, 4, 5]
newList01 = list(filter(even, thisList))  # use-function-in-filter
print(newList01)

newList02 = list(filter(lambda a: a % 2 == 0, thisList))  # use-lambda-in-filter
print(newList02)
