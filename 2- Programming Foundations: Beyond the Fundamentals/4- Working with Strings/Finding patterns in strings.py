# Worling with strings

first_name = "Muhammad"
last_name = "Selim"
first = first_name.capitalize()
last = last_name.capitalize()
print("Name is " + first + " " + last)


"""
-> Finding text:
.find()
.index()
.rfind()
.rindex()
"""
s = "This is a string I want to search"
print(s.find("want")) # retuens the index of first char in the required string, here is 19.


"""
-> Slicing: geting part of a string value
    string[start:end]
"""
ss = "This is a string I want to search"
new_string = s[17:] # get slice of string, "I want to search", form index 17 to end
print(new_string)