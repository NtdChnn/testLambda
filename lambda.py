def multiply(a, b, c):
    return a * b * c


multiply_l = lambda a, b, c: a * b * c

print(multiply(5, 6, 7))  # use-function
print(multiply_l(5, 6, 7))  # use-lambda
