from functools import partial

nested_list = [['Hello', 'World'], ['Goodbye', 'World']]
nested_list = list((map(partial(map, str.upper), nested_list)))
print(nested_list)
