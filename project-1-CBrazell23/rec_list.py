# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist):
    if(strlist is None): # Checks if strlist is None in which case it returns None
        return None
    if(strlist.rest is None): # Checks for None in which case the value is returned
        return strlist.value
    if(strlist.value < first_string(strlist.rest)): # Compares the value to the rest put through the function recursively
        return strlist.value
    else: # Continues otherwise
        return first_string(strlist.rest)

    return smallestWord

# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist):
    if(strlist is None): # Base case that returns a tuple of Nones upon reaching None
        return (None, None, None)

    returnTup = split_list(strlist.rest) # Creates tuple that adds value into correct place based on criteria

    if(strlist.value[0] in 'aeiou' or strlist.value[0] in 'AEIOU'): # Checks if first char is a vowel
        return (Node(strlist.value, returnTup[0]), returnTup[1], returnTup[2])
    if(strlist.value[0] not in 'aeiou'and strlist.value[0] not in 'AEIOU' and strlist.value.isalpha()): # Checks if first char is a consonant
        return (returnTup[0], Node(strlist.value, returnTup[1]), returnTup[2])
    if(strlist.value[0].isalpha() == False): # Checks if first char is not an alpha character
        return (returnTup[0], returnTup[1], Node(strlist.value, returnTup[2]))
