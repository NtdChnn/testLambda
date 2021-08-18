def square(a):
    return a ** 2


thisList = [1, 1, 2, 3, 4, 5]
newList01 = list(map(square, thisList))  # use-function-in-map
# print(newList01)
newSet01 = set(map(square, thisList))  # return-set
# print(newSet01)
newTuple01 = tuple(map(square,  thisList))  # return-tuple
# print(newTuple01)

newList02 = list(map(lambda a: a ** 2, thisList))  # use-lambda-in-map
# print(newList02)

thisList01 = [1, 2, 3]
thisList02 = [4, 5, 6]
newList03 = list(map(lambda a, b: a+b, thisList01, thisList02))  # two-parameters
# print(newList03)
