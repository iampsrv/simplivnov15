# # # datascientist = set(['Python','R', 'SQL', 'Git', 'Tableau','SAS'])
# # # dataengineer= set(['Python','Java','Scala','SQL', 'Git','Hadoop'])

# # # # print(datascientist.intersection(dataengineer))
# # # # print(datascientist.difference(dataengineer))
# # # # print(dataengineer.difference(datascientist))
# # # # print(datascientist.union(dataengineer))
# # # print(datascientist.symmetric_difference(dataengineer))


# # # removing duplicate values

# # my_list= [1,2,3,1,2,3,4,5,6,7,1,1,1,1,1,1]
# # print(list(set(my_list)))

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# is_subset = set1.issubset(set2)
# print(is_subset)

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# is_superset = set1.issuperset(set2)
# print(is_superset)

# my_set = {1, 2, 3}
# print(my_set)
# my_set.add(4) # Adding a single element to the set
# print(my_set)
# my_set.update([5, 6, 7]) # Adding multiple elements to the set
# print(my_set)

my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.remove(3) # Removing an element from the set
print(my_set)
my_set.discard(6) # Removing an element if it exists, without raising an error
print(my_set)
my_set.pop()
print(my_set)