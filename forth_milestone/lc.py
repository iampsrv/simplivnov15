num = [1,2,3,4,5,6]

even =[]
for a in num:
    if a %2==0:
        even.append(a)
print(even)

print([a**2 for a in num if a % 2==0])