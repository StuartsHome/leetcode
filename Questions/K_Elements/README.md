# K Elements
Find K smallest
- Sort ascending order - `O(n log n)` (quick sort, merge sort)
- Max heap -  
    - Finding largest elements - `O(1)`
- Hoare's Selection Algorithm (Quickselect)
    - Average Time Complexity: O(N)
    - Worst Case: O(N^2)


## Top K Frequent Elements
Steps:
- Build hash map of frequency - O(N) where N is the number of elements in the list
- Build heap of size K using N elements - O(N log K)
- Convert heap to output array - O(K log K)




### Quickselect
- Choose a pivot and define its position in a sorted array in a linear time using partition algorithm
```python
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index
        
        def quickselect(left, right, k_smallest):
            # base case: the left contains only one element
            if left == right:
                return
            # select a random pivot_index
            pivot_index = random.randint(left, right)
            
            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index -1, k_smallest)
            
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)
        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent. 
        quickselect(0, n-1, n-k)
        return unique[n-k:]
```
Steps -
1. Get list of frequencies
2. Convert keys into unique array
3. Call quickselect to choose random int in unique to be pivot_index
4. Call partition with pivot_index
    1. Partitions goal is to place pivot in correct position
5.  Move pivot to the end
6. Set the pointer at the beginning of the array store_index = left.
7. Iterate over the array and move all less frequent elements to the left swap(store_index, i). Move store_index one step to the right after each swap.
8. Move the pivot to its final place, and return this index. 
9. Compare pivot_index and N - k.
    1. If pivot_index == N - k, the pivot is N - kth most frequent element, and all elements on the right are more frequent or of the same frequency. Return these top kk frequent elements.
    2. Otherwise, choose the side of the array to proceed recursively.