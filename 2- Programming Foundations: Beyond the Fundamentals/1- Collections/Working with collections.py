# list items can be accessed by index starting from 0 to n-1, where n is the number of items in list
cities = [
    'Cairo',
    'Alex',
    'Dublin',
    'Helsinki'
]
# to get the second item, here is Alex, we do that:
print(cities[1]) # -> Alex

# dictionary items can be accessed by name of its key
my_information = {
    'name': 'Muhammad Ahmad',
    'age': 20,
    'color': 'orange'
}
print(my_information['name']) # -> Muhammad Ahmad



# more advance
data = {
    'names': ['Muhammad', 'ahmad', 'ali'],
    'id': [1, 2, 3],
    'grade': ['A+', 'B+', 'A']
}
print(data['names']) # -> ['Muhammad', 'ahmad', 'ali']
print(data['grade'][1]) # -> B+ it gets the grade of second person in list 