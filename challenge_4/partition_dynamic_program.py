'''
For this input:
    XXXX

The optimal solution is:
    YYYY

The [values] included for this optimal solution are: 
    ZZZZ
'''

'''
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.

Following are the two main steps to solve this problem:
1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.

'''

'''
Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
there is a subset of arr[0..n-1] with sum equal to sum/2
'''

def isSubsetSum(arr, n, sum):
    print(arr)
    print(sum)
    #base case
    if sum == 0:
        return True

    if n == 0 and sum != 0:
        return False

    if arr[n-1] > sum: 
        return isSubsetSum (arr, n-1, sum) 

    with_last_element = isSubsetSum(arr, n-1 , sum)
    without_last_element = isSubsetSum(arr, n-1, sum - arr[n-1])

    # return whichever is true
    return with_last_element or without_last_element


def partition(arr, length):
    
    sum = 0

    for i in arr:
        sum += i 

    if sum % 2 != 0:
        return False
    
    return isSubsetSum(arr, length, sum/2)

if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    length = len(arr)
    print(partition(arr, length))
