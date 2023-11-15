# person = {
# "name": "Pranjal",
# "age": 25,
# "skill": ["python","java"]
# }

# person["age"]=26
# person["city"]="Mumbai"
# print(person)
# print(person.values())

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}
print(merged_dict)