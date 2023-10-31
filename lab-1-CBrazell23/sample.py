# Some simple sample functions

# integer -> integer
# Returns factorial of input n
def factorial(n): # assumes n non-negative integer, a number
    if (n == 0) :
        return 1
    else:
        return n * factorial(n-1)

# integer -> integer
# Returns nth Fibonacci number
def fib(n):
    """ Assumes n is non-negative integer"""
    if ((n == 1) or (n == 0)):
        return n
    else:
        return fib(n-1) + fib(n-2)

# List -> value
# Returns max of an input list (tlist) of numbers
def maxlist_rec(tlist):
    if (len(tlist) == 0):
        raise ValueError('empty list')
    elif (len(tlist) == 1):
        return tlist[0]
    else:
        templist = tlist[1:len(tlist)]
        temp = maxlist_rec(templist)
        return (max(tlist[0],temp))

# String -> String
# Iteratively reverses a string
def reverse_iter(tempstring):
    newstring = ""
    for i in range(len(tempstring)-1,-1,-1)  :
        newstring = newstring + tempstring[i]
    return newstring
