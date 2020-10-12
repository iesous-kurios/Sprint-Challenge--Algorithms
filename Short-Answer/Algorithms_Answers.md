#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
Runtime: 'O(n)'
Reasoning: Each iteration increases by n^2, and it is looking for 'a' to be greater than n^3.  
n^3 divided by n^2 gives us n, so O(n) runtime complexity.  

b)
Runtime: 'O(n log n)
Reasoning: The outer portion is 'O(n)', and the inner begins at 1 then doubles until it is greater than
n, giving it a O(log2 n) complexity.  Nested loops have their complexity multiplied, giving us O(n log n)

c)
Runtime: 'O(n)'
Reasoning: This algorithm calls itself recusrively.  A constant amount is subtracted each time, bringing 
it closer and closer to the base case of 0.  Due to the constant amount, and only one recursive call each iteration,
the number of steps will mimic a linear function.  

## Exercise II

The total amount of floors can be considered as an array of elements.  I would write a function
that starts halfway in the array (after sorting, if needed)

When an egg is dropped and breaks, that lets me know the floor is too high

When an egg is dropped and doesn't break, that tells us that we are at or below the sweet spot
for how many floors before an egg breaks.  

All that considered:

1. Determine maximum amount of floors
2. Determine minimum amount of floors

3. Start at middle of min and max
4. Drop an egg
5. If egg broke, start again from step 3
6. If egg did not break, set min floor to current floor: start again from number 3 
7. If egg breaks, return f = the previous floor
8. If egg does not break, start again from number 6
9. return f

This would basically be me implementing a binary search tree.  Since BSTs halve themselves at 
each step, we will have a O(log n) complexity