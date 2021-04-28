from itertools import zip_longest, chain, tee
def replace2copy(ls):
    lst1, lst2 = tee(iter(ls), 2)
    return list(chain.from_iterable(zip_longest(ls[1::2], ls[::2])))
n = [0,1,2,3,4,5,6,7]
print(replace2copy(n))
