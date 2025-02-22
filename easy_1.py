# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def function(the_list: list, the_number: int) -> bool:
    """
    Add each number on the list with every following number
    Create a list of booleans that checks if the sum of the two numbers is equal to the_number
    Check if any of the elements on the list is True and return it else return False
    """
    return True if any([the_list[x] + the_list[y] == the_number for x in range(len(the_list)-1) for y in range(x+1, len(the_list))]) else False

print(function([10, 15, 3 ,7], 17))