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

Top:
- Camelcase Matching - Leetcode 1023
- Subsequence
    - Longest Common Subsequence - [recursion & dp] - Leetcode 1143
        - Recursion w/ memo T: O(mn)
        - Bottom up DP T: O(mn), S: O(mn)
    - Longest Increasing Subsequence - [recursion & dp]- Leetcode 674
        - recursion T: O(2^n), S: O(n^2) - size of recursion tree is 2^n, memo array of size n * n is used
        - dp T: O(n^2), S: O(n) - Two loops of n, dp of size n