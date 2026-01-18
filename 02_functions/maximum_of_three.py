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

help(max_of_three)