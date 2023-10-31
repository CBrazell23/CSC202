from stack_array import *

# You should not change this Exception class
# Exception class that we can raise with our own messages
class PostfixFormatException(Exception):
    pass

# Method that evaluates a postfix expression
# str --> int
def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    length = len(input_str)
    if(length < 3): # Checks if there are enough operands
        raise PostfixFormatException("Insufficient operands")
    word = input_str.split() # Splits string into list
    check = input_str.replace(" ", "")
    for x in check: # Checks to make sure all tokens are valid
        if(x not in "0123456789+-**/<<>>."):
            raise PostfixFormatException("Invalid token")
    try: # Try block to catch invalid format exceptions
        stk = Stack(length)
        for y in word:
            if("." in y): # Converts y to float if possible
                try:
                    y = float(y)
                except ValueError:
                    pass
            if(not isinstance(y, float)): # Converts y to int if possible
                try:
                    y = int(y)
                except ValueError:
                    pass
            if(isinstance(y, int) or (isinstance(y, float))):
                stk.push(y)
            elif(y == "+"):
                a = stk.pop()
                b = stk.pop()
                stk.push(b + a)
            elif(y == "-"):
                a = stk.pop()
                b = stk.pop()
                stk.push(b - a)
            elif(y == "*"):
                a = stk.pop()
                b = stk.pop()
                stk.push(b * a)
            elif(y == "/"):
                a = stk.pop()
                b = stk.pop()
                stk.push(b / a)
            elif(y == "**"):
                a = stk.pop()
                b = stk.pop()
                stk.push(b ** a)
            elif(y == "<<"):
                a = stk.pop()
                b = stk.pop()
                if(isinstance(a, float) or isinstance(b, float)):
                    raise PostfixFormatException("Illegal bit shift operand")
                stk.push(b << a )
            elif(y == ">>"):
                a = stk.pop()
                b = stk.pop()
                if (isinstance(a, float) or isinstance(b, float)):
                    raise PostfixFormatException("Illegal bit shift operand")
                stk.push(b >> a)
        fin = stk.pop()
        if(not stk.is_empty()):
            raise PostfixFormatException("Too many operands")
    except IndexError:
        raise PostfixFormatException("Insufficient operands")
    except ZeroDivisionError:
        raise ValueError
    return fin




    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""

# Converts an infix expression to a postfix expression
# str --> str
def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""
    length = len(input_str)
    returnStr = ""
    word = input_str.split()
    check = input_str.replace(" ", "")
    for x in check:
        if(x not in "0123456789+-**/<<>>.()"):
            raise PostfixFormatException("Invalid token")
    stk = Stack(length)
    for y in word:
        if("." in y):
            try:
                y = float(y)
            except ValueError:
                pass
        if(not isinstance(y, float)):
            try:
                y = int(y)
            except ValueError:
                pass
        if(isinstance(y, int) or (isinstance(y, float))):
            returnStr += str(y)
            returnStr += " "
        elif(y == "("):
            stk.push(y)
        elif(y == ")"):
            popped = ""
            bool = True
            while(bool): # Pops all relevant operators until '(' is reached
                popped = stk.pop()
                if(popped == "("):
                    bool = False
                else:
                    returnStr += str(popped)
                    returnStr += " "
        else:
            if(stk.is_empty()):
                stk.push(y)
            elif(y == "*" or y == "/"): #left
                if(stk.peek() in "**/"): #Possibly */+-
                    returnStr += str(stk.pop())
                    returnStr += " "
                    stk.push(y)
                else:
                    stk.push(y)
            elif(y == "+" or y == "-"): #left
                if(stk.peek() in "+-**/"):
                    returnStr += str(stk.pop())
                    returnStr += " "
                    stk.push(y)
                else:
                    stk.push(y)
            elif(y == "<<" or y == ">>"): #left
                if(stk.peek() in "+-*/>><<"):
                    returnStr += str(stk.pop())
                    returnStr += " "
                    stk.push(y)
                else:
                    stk.push(y)
            elif(y == "**"): #right
                stk.push(y)
    while(not stk.is_empty()):
        returnStr += str(stk.pop())
        returnStr += " "
    return returnStr.strip()

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """

# Converts a prefix expression to a postfix expression
# str --> str
def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    length = len(input_str)
    returnStr = ""
    word = input_str.split()
    word = word[::-1] # Reverses string
    check = input_str.replace(" ", "")
    for x in check:
        if (x not in "0123456789+-**/<<>>.()"):
            raise PostfixFormatException("Invalid token")
    stk = Stack(length)
    for y in word:
        if("." in y):
            try:
                y = float(y)
            except ValueError:
                pass
        if(not isinstance(y, float)):
            try:
                y = int(y)
            except ValueError:
                pass
        if(isinstance(y, int) or (isinstance(y, float))):
            stk.push(str(y))
        elif(y in "+-**/<<>>"):
            a = stk.pop()
            b = stk.pop()
            concat = ""
            concat += str(a)
            concat += " "
            concat += str(b)
            concat += " "
            concat += y
            concat += " "
            returnStr += concat
            stk.push(concat)
    fin = stk.pop()
    fin = fin.strip()
    return fin.replace("  ", " ")

    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""


