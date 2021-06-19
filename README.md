# Info
## :wrench: README included in:
- Binary_Search
- Graphs
- K_Elements
- Knapsack_Problems
- Kneedle in Haystack
- Linked List
- Palindrome
- Permutations
- Subsequence
- Trees
- Tries

## Time Complexity
Questions:
- What's the time complexity of each recursive call?
- How many times each recursive call invoked?


## Bounds on Asymptotic Growth Rates
- Upper bound: Big O
- Tight bound: Upper case Theta
- Lower bound: Big Omega


## Space Complexity
For recursive solutions, the space complexity is the stack space occupied by all the recursive calls.


Top:
- Camelcase Matching - Leetcode 1023
- Subsequence
    - Longest Common Subsequence - [recursion & dp] - Leetcode 1143
        - Recursion w/ memo T: O(mn)
        - Bottom up DP T: O(mn), S: O(mn)
    - Longest Increasing Subsequence - [recursion & dp]- Leetcode 674
        - recursion T: O(2^n), S: O(n^2) - size of recursion tree is 2^n, memo array of size n * n is used
        - dp T: O(n^2), S: O(n) - Two loops of n, dp of size n



### Algorithms
- Binary Indexed Tree (Fenwick Tree)
    - Used to efficiently calculate prefix sums (accumulation sum)
    - Leetcode 307: Range Sum Query - Mutable


