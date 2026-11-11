list1 = [1, 2, 3, 4, 5]

list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

first_only = set1.difference(set2)

all_unique = set1.union(set2)

print("Common elements:", common)

print("Only in first list:", first_only)

print("All unique elements:", all_unique)
