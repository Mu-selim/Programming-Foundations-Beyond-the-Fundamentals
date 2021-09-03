# Nearest stars to Earth
star1 = 'Sol'
star2 = 'Alpha Centauri'
star3 = 'Barnard'
star4 = 'Wolf 359'

# Highest peak on each tectonic plate
African = 'Kilimanjaro'
Antarctic = 'Vinson'
Australian = 'Puncak Jaya'
Eurasian = 'Everest'
North_American = 'Denali'
Pacific = 'Mauna Kea'
South_American = 'Aconcagua'

"""
Challenge:
for first group of variables
    1.Replace variables with list "stars"
    2.Create statement that prints fourth nearest star
for first group of variables
    1.Create dictionary "peaks" that stores all values
    2.Create statement that prints name of highest peak on Pacific plate
"""

# Solution
stars = [
    'Sol',
    'Alpha Centauri',
    'Barnard',
    'Wolf 359'
]
print('The fourth nearest star to Earth is', stars[3])

peaks = {
    'African': 'Kilimanjaro',
    'Antarctic': 'Vinson',
    'Australian': 'Puncak Jaya',
    'Eurasian': 'Everest',
    'North_American': 'Denali',
    'Pacific': 'Mauna Kea',
    'South_American': 'Aconcagua'
}
print('The highest peak on Pacific plate is', peaks['Pacific'])