# This function will assign random values from a list to another list.
# It unfortunately will sometimes have duplicates. Especially if 'assignment' 
#is smaller than 'arr'
def assign_random(arr,assignment):
    import random
    new_assignment = map(lambda x: random.choice(assignment),arr)
    return new_assignment

# This function will assign random values from a list to another list.
# This one should not have duplicates, but it will throw an error if 
# len(arr) > len(assignment)
def assign_random2(arr,assignment):
    import random
    if len(arr) > len(assignment):
        return "Error: Random samples must be greater than input array."
    new_assignment = random.sample(assignment,len(arr))
    return new_assignment

#Example    
arr = ['Bob','Steve','Doug','Mary']
assignment = ['Mr. White','Mr. Pink','Mr. Brown','Mr. Blonde','Mr. Orange','Mr. Blue']
print assign_random(arr,assignment)
print assign_random2(arr,assignment)