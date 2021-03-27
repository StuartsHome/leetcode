# Info

## Topics

### DP (Dynamic Programming)
- DP = Recursion + Memoization + Guessing
- DP doesn't work on graphs with cyles. This is because the memo table hasn't finished computing when it's called again, resulting in an infinite loop.
- For (DAGS) cylic graphs it's ok
- Bottom-up algos do a topological sort of the dependency DAG (acyclic)

### Paths
Find shortest path between Source `(s)` and target `(v)` for all `(v)`
- The memoized algorithm does a DFS, to do a Topological sort, to run one round of Bellman Ford




Find shortest path between Source `(s)` and target `(v)`
This is a single target shortest path

