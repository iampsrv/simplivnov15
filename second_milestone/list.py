# # my_list = list(range(1, 20,2))


# # # #length of list
# # # len_of_list= len(my_list)

# # # # accessing the elements of list
# # # print("first element is ",my_list[0])
# # # print("first element is ",my_list[-len_of_list])
# # # print("last element is ",my_list[len_of_list-1])


# # # # modifying the elements of list
# # # print("before modification")
# # # print(my_list)
# # # my_list[0]=0
# # # my_list.append(21)
# # # my_list.extend([23,25])
# # # print("after modification")
# # # print(my_list)


# # # Slicing

# # # print(my_list)
# # # print(my_list[2:6])

# # # Reversing
# # # print(my_list[::-1])
# # # print(my_list)
# # # Removing elements
# # # my_list.remove(1)
# # # del my_list[0]
# # # my_list.pop()
# # # print(my_list)


# # # my_new_list =[]

# # # for i in my_list:
# # #     my_new_list.append(i**2)

# # # print(my_new_list)

# # # Merging
# # list1 = [1, 2, 3]
# # list2 = [4, 5, 6]
# # concatenated_list = list1 + list2
# # print(concatenated_list)

# my_list = [4, 2, 1, 3, 5]
# my_list.sort() # Sorting the list in ascending order
# my_list.sort(reverse=True) # Sorting the list in descending order
# print(my_list)

marks = [80,85,90,100,95]
print("Minimum marks is {}".format(min(marks)))
print(max(marks))
print(sum(marks))
print(sum(marks)/len(marks))
print(marks)
marks.insert(1,99)
print(marks)

