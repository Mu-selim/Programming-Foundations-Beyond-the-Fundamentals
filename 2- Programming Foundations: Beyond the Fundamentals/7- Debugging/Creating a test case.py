"""
-> Test Cases:
    commands or scripts designed to test a specific scenario
"""

def test_high_of_tree(high):
    if high <= 2:
        print("The tree is short")
    elif high >= 2 and high <= 5:
        print("The tree is medium")
    elif high > 5:
        print("The tree is huge")

test_high_of_tree(1.5)
test_high_of_tree(4.6)
test_high_of_tree(7)