# Write a Python function to find the maximum of three numbers.

#---First attempt---
def max_of_three_numbers(num1,num2,num3):
    maximum = 0
    if num1 > num2 and num3: # num1 > num2 wordt vergeleken, dat is 7. daarna staat er eigenlijk 7 and 3, het doet niets behalve dat ze allebei True geven.
        maximum = num1       # daarna wordt er gezegd dat maximum 7 wordt
    if num2 > num1 and num3: # num2 > num1 wordt vergeleken, dat is False, daarna staat er eigenlijk False and 3. 3 is True want het is geen 0, dus er staat False and True.
        maximum = num2       # omdat False and True, False geeft wordt er niets veranderd aan maximum
    if num3 > num1 and num2: # num3 > num1 wordt vergeleken, dat is 3 en is False, daarna staat er eigenlijk False and 2, dus False and True.
        maximum = num3       # er wordt niets veranderd aan maximum omdat de vergelijking False is
    return maximum

print(max_of_three_numbers(7,2,3))

#---Try with 2 numbers first---

#def max_of_two(x,y):
#    if x > y:
#        return x
#    elif y > x:
#        return y

#---max of three v1---
#def max_of_three(x,y,z):
#    if z < x > y:
#        return x
#    elif x < z > y:
#        return z
#    else:
#        return y
#print(max_of_three(10,3,6))

#---max of three v2---
#def max_of_three(x,y,z):
#    if max_of_two(x,y) > z:
#        return max_of_two(x,y)
#    else:
#        return z
#print(max_of_three(10,3,6))

# Try with  2 numbers first
def max_of_two(x,y):
    """
    Returns the maximum of two numbers

    :param x: first number
    :param y: second number
    :return: the larger of x and y
    """
    if x > y:
        return x
    return y            # Outside the if-statement is the same as 'else'


def max_of_three(x,y,z):
    """
    Returns the maximum of three numbers

    :param x: first number
    :param y: second number
    :param z:  third number
    :return: the larger of x, y and z
    """
    return max_of_two(x, max_of_two(y,z))
print(max_of_three(55,3,88))

#help(max_of_three)
#_______________________________________________________________________________________________________________________________________
# Write a Python function that takes three parameters and returns the largest using nested ternary operators.
# It is basically an if-else statement in one line

def max_of_three_v2(x,y,z):
    return x if x > y and x > z else z if z > x and z > y else y
  # return x if (x > y and x > z) else (z if (z > x and z > y) else y) parentheses are optional but is better for readability

#_______________________________________________________________________________________________________________________________________
# Write a Python function that finds the maximum of three numbers without using the built-in max() function by using if-else statements.

def max_of_three_v1(x,y,z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

#_______________________________________________________________________________________________________________________________________
# Write a Python function that accepts three numbers in a list and uses recursion to determine the maximum value.

def max_of_three_v3(list_of_numbers):
    if len(list_of_numbers) == 1:     # You start with the base case when the program should end executing te function.
        return list_of_numbers[0]     # In this case, stop when the list has only one list item

    first_list_item = list_of_numbers[0]                        # Define variables (first list item)
    rest_of_list_items = max_of_three_v3(list_of_numbers[1:])   # Rest of the list items, if you enter 3 numbers than the last 2 list items are stored here

    if first_list_item > rest_of_list_items: # check if the first list item is greater than de rest of the listitems
        return first_list_item # if the first list item is greater than the rest, it will be entered in the function again.
    else:
        return rest_of_list_items # if the first list item was not greater than de rest of the list items, these items are entered into the function to go through the whole proces again until there is only one list item left

print(max_of_three_v3([10,25,7]))
# Source: This video helped me understand recursions https://www.youtube.com/watch?v=GEcG_esvl9Y
#_______________________________________________________________________________________________________________________________________
# Write a Python function that sorts three numbers and returns the last element as the maximum, ensuring the original order is preserved.
def sort_numbers(x,y,z):
    numbers = [x,y,z]
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1]

print(sort_numbers(9,2,8))

