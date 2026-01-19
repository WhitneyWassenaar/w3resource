# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_all_numbers_in_list(number_list):
    """
    Sum all numbers in a list by using the sum() function

    :param number_list:
    :return: sum(number_list)
    """
    return sum(number_list)

numbers = [8,2,3,0,7]
print(sum_all_numbers_in_list(numbers))


def sum_function(number_list):
    """
    Sum all numbers in a list by counting them manually

    :param number_list:
    :return: total
    """
    total = 0
    for number in number_list:
        total += number
    return total
print(sum_function([8,2,3,0,7]))

#_______________________________________________________________________________________________________________________________________
# Write a Python function that uses a for-loop to sum all numbers in a list and returns the total

def sum_numbers(numbers):
    """
    Sum all numbers in a list and return total

    :param numbers: List with numbers to sum
    :return: total
    """
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_numbers([2,4,5,6]))

#_______________________________________________________________________________________________________________________________________
# Write a Python function that uses recursion to compute the sum of all elements in a list.
def sum_recursion(sum_list):
    """
    Compute sum with recursion
    sums integers in a list, one by one until there is no integer left

    :param sum_list: list of integers
    :return:
    """
    if sum_list == []:
        return 0

    return sum_list[0] + sum_recursion(sum_list[1:])

print(sum_recursion([2,4,5,6]))

#_______________________________________________________________________________________________________________________________________
# Write a Python function that uses the built-in sum() function to sum a list, then compare its output with a manually computed sum.
def sum_function(enter_list):
    """
    Use sum() and compare its output with a manually computed one

    :param enter_list: list of integers
    :return: True or False, is the output of sum() the same as function:def sum_numbers(numbers)?
    """
    sum_list = sum(enter_list)
    return sum_list == sum_numbers(enter_list)
print(sum_function([5,5,5]))

#_______________________________________________________________________________________________________________________________________
# Write a Python function that sums only the positive numbers from a list and ignores negatives, using list comprehension.
def sum_positives(any_numbers):
    """
    Sum only positives from a list, ignores negatives in a list with list comprehension

    :param any_numbers: list of integers(positive and negative)
    :return: sum of only the positive integers
    """
    sum_only_positives = [any_number for any_number in any_numbers if any_number > 0]
    return  sum(sum_only_positives)
print(sum_positives([5,-5,5]))

# It's incorrect to use a sum() function inside a list comprehension:
# example: sum_only_positives = [sum(any_number for any_number in any_numbers if any_number > 0)]