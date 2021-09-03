"""
-> Regular expression "Regex":
    Allows you to create a description of a pattern that
    you want to match

-> Regular expression or Regex:
    can be made up of letters, numbers and special characters
"""

import re
five_digit = "10189"
nine_digit = "3000-10189"
number_of_phone = "010-124-6789"

fiveD_expression = r"\d{5}" # we want five digit in a row

print(re.search(fiveD_expression, five_digit))
print(re.search(fiveD_expression, nine_digit))
print(re.search(fiveD_expression, number_of_phone))