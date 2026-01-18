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
