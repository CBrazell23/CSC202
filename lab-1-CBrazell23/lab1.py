# CPE 202 Lab 1

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
#Finds the largest value in a list
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if (int_list == None):
        raise ValueError
    elif ((len(int_list)) < 1):
        return None
    else:
        max = int_list[0]
        for i in range(1, len(int_list), 1):
            if (int_list[i] > max):
                max = int_list[i]
    return max


# Maybe_List -> Maybe_List
#Reverses a list using recursion
def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list == None:
       raise ValueError
    else:
       if len(int_list) <= 1:
           return int_list
       return reverse_rec(int_list[1:]) + [int_list[0]]



# integer, integer, integer, Maybe_List -> integer
#Performs a binary search
def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if(int_list == None):
        raise ValueError
    elif target not in int_list:
        return None
    else:
        mid = (high + low) / 2
        if(mid == target):
            return mid
        elif(mid < target):
            bin_search(target, low, mid, int_list[:mid])
        else:
            bin_search(target, mid, high, int_list[mid:])