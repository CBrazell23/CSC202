# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    returnList = [] # Initiates return list
    if(len(str_in) == 0): # Checking for empty string
        return []
    elif(len(str_in) == 1): # Base case once length of input is one
        return str_in
    else:
        for i in range(0, len(str_in), 1):
            rm = str_in[i] # Separates individual chars in string
            word = str_in[:i] + str_in[i + 1:]
            split = perm_gen_lex(word)
            for x in split:
                returnList.append(rm + x) # Appends the individual char and the permutations to the return list
                #returnList += (rm + x)
    return returnList