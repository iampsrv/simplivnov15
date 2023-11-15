# str1 = "Hello"
# str2 = "World"
# result = str1 + " " + str2 # Concatenating two strings with a space in between
# print(result)

# name = "Pranjal"
# age = 25
# message = "My name is {} and I'm {} years old.".format(name, age)
# print(message)

# text = "I love java programming"
# new_text = text.replace("java", "Python")
# print(new_text)

# words = new_text.split(" ")
# print(words)

text = "P7y8t9h6o4n"
digits = ''.join(filter(str.isdigit, text))
letters = ''.join(filter(str.isalpha, text))
print(digits) # Output: "78964"
print(letters) # Output: "Python"