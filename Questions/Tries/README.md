Tries and hash tables are reminiscent of one another because they both use arrays under the hood.
- Tries - arrays combined with linked liasts
- Hash Tables - arrays combined with pointers/references

Differences
- Tries contain no hash function (no collisions)
This is because each key can be represented in alphabetical order, and is uniquely retrievable since\
every branch path to a string's values will be unique to that key.
- Disadvantage - takes up a lot of memory and space will empty (null) pointers.

### Time complexity
- O(mn) (m = length of longest key in trie, n = total number of keys in trie)
The amount of time it takes to create a trie is tied directly to how many words/keys the trie contains, and how long those keys could potentially be. The worst-case runtime for creating a trie is a combination of m, the length of the longest key in the trie, and n, the total number of keys in the trie. Thus, the worst case runtime of creating a trie is O(mn).

The time complexity of searching, inserting, and deleting from a trie depends on the length of the word a that’s being searched for, inserted, or deleted, and the number of total words, n, making the runtime of these operations O(an). Of course, for the longest word in the trie, inserting, searching, and deleting will take more time and memory than for the shortest word in the trie.