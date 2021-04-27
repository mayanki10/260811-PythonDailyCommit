def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'a': 1, 'b': 8}
dict2 = {'d': 2, 'c': 4}
print(Merge(dict1, dict2))
print(dict2)