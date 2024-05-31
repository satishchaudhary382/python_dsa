#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false

#As usual we'll get the naive approach out of the way first.

def brute_force_duplicate(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            print(i,j)
            if array[i] == array[j]:
                return True
            else:
                return False

array =  [1,2,32,98,61,34,46]
print(brute_force_duplicate(array))