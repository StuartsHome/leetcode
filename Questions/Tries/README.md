Tries and hash tables are reminiscent of one another because they both use arrays under the hood.
- Tries - arrays combined with linked liasts
- Hash Tables - arrays combined with pointers/references

Although hash table has O(1) time complexity for looking for a key, it is not efficient in the following operations :

- Finding all keys with a common prefix.
- Enumerating a dataset of strings in lexicographical order.

Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to O(n)O(n), where nn is the number of keys inserted. Trie could use less space compared to Hash Table when storing many keys with the same prefix. In this case using trie has only O(m)O(m) time complexity, where mm is the key length. Searching for a key in a balanced tree costs O(m \log n)O(mlogn) time complexity.

Differences
- Tries contain no hash function (no collisions)
This is because each key can be represented in alphabetical order, and is uniquely retrievable since\
every branch path to a string's values will be unique to that key.
- Disadvantage - takes up a lot of memory and space will empty (null) pointers.

### Time complexity
- O(mn) (m = length of longest key in trie, n = total number of keys in trie)
The amount of time it takes to create a trie is tied directly to how many words/keys the trie contains, and how long those keys could potentially be. The worst-case runtime for creating a trie is a combination of m, the length of the longest key in the trie, and n, the total number of keys in the trie. Thus, the worst case runtime of creating a trie is O(mn).

The time complexity of searching, inserting, and deleting from a trie depends on the length of the word a that’s being searched for, inserted, or deleted, and the number of total words, n, making the runtime of these operations O(an). Of course, for the longest word in the trie, inserting, searching, and deleting will take more time and memory than for the shortest word in the trie.