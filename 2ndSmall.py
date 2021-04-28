def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_it = set()
  uniq_it = []
  for x in numbers:
    if x not in dup_it:
      uniq_it.append(x)
      dup_it.add(x)
  uniq_it.sort()
  return  uniq_it[1]

print(second_smallest([4, 3, -8, -2, 0, -1]))
print(second_smallest([1, 1, 0, 3, 2, -2, -3]))
print(second_smallest([1, 1, 1, 0, 1, 0, 2, -2, -2]))
print(second_smallest([2,-3]))
print(second_smallest([-1]))