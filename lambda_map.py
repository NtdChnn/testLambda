def square(a):
    return a**2


thisList = [1, 2, 3, 4, 5]
newList01 = list(map(square, thisList))  # use-function-in-map
print(newList01)

newList02 = list(map(lambda a: a**2, thisList))  # use-lambda-in-map
print(newList02)
