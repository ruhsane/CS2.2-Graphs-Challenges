# Problem 1
Knapsack - find the most amount of items with the most value that you can fit in a bag with a fixed capacity.

## Reference
[Class Slide](https://docs.google.com/presentation/d/1QoK6PMX0eiJ6XEQsKa5ZkU-_EJHZ-uG1Pc6attOBkAQ/edit#slide=id.g5e24cbf5a7_0_189)

## 5 Steps of Dynamic Programming as applied to this problem
1. Identify the subproblems
whether to take the current item or not.

2. Guess first choice
start with any item

3. Recursively define the value of an optimal solution
get the total value of the bag including the current item until it reaches capacity

4. Compute the value of an optimal solution (recurse and memoize)
get the total value of the bag without the current item until it reaches capacity

5. Solve original problem - reconstruct from the sub-problems
calculate to see which one of the above two calculations gives me higher value, and choose accordingly. At the end, choose the combination with the highest value.

# Problem 2
Partition - Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

Examples:
```
arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
```

## Reference
https://www.geeksforgeeks.org/partition-problem-dp-18/


