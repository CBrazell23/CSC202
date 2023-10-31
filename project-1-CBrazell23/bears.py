# int -> booelan
# Given integer n (number of bears initially), returns True or False based on reachabilty of goal of attaining 42 bears
def bears(n):
    if(n == 42): # Base case that once n is 42 returns True because the goal has been reached
        return True
    elif(n < 42): # Checking to make sure that n remains greater than 42 as any lower would indicate an inability to attain the goal
        return False
    else:
        if (n % 2 == 0):  # Case that n is even in which case we divide n by 2
            if (bears(n / 2)):
                return True
        if (n % 3 == 0 or n % 4 == 0): # Case that n is divisible by 3 or 4 in which case we multiply the last two digits
            x = n % 10 # Finds the last digit
            y = n % 100 # Finds the last two digits
            if (x != 0 and y // 10 != 0): # Making sure the last digit and the second to last digit are not 0
                if (bears(n - (x * y // 10))):
                    return True
        if(n % 5 == 0): # Case that n is divisible by 5 in which case we need to run it with 42 less bears
            if(bears(n - 42)):
                return True
    return False