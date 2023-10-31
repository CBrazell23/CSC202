import random
import time

# Function that sorts a list using the selection sort algorithm
# list --> int
def selection_sort(l):
    counter = 0
    if(len(l) <= 1):
        return 0
    for i in range(len(l) - 1, 0, -1):
        pos = 0
        for j in range(1, i + 1):
            counter += 1
            if(l[j] > l[pos]):
                pos = j
        temp = l[pos]
        l[pos] = l[i]
        l[i] = temp
    return counter

# Function that sorts a list using the insertion sort algorithm
# list --> int
def insertion_sort(l):
    counter = 0
    if (len(l) <= 1):
        return 0
    for i in range(1, len(l)):
        cur = l[i]
        j = i
        counter += 1
        while(j > 0 and l[j - 1] > cur):
            l[j] = l[j - 1]
            j = j - 1
            counter += 1
            if(j == 0):
                counter -= 1
        l[j] = cur
    return counter


def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

