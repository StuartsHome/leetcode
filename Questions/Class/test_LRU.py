
# LL node contains: new_node -> LinkedNode(value, key)
# Dictionary -> value is the LinkedNode
# To update the value in cache, we have to update the value contained within the associated LinkedNode
# To update the dictionary value -> dict[curr].
class LinkedNode:
    pass

class cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memo = {}
        self.head = LinkedNode()
        self.tail = LinkedNode()

    def getter(self, key):
        curr = self.memo

        if key in curr:
            if curr[key] != self.tail:  # Test if key is tail of LL, if yes, no need to update
                pass
                # remove from LL
                # add key to LL
            return curr[key].val
        else:
            return -1
        
    def put(self, key, value):
        curr = self.memo

        if key in curr:
            curr[key].val = value
            self.get(key)
            # add to 

            return
        else:
            if len(cache) == self.capacity:
                # remove head key from LL and pass to head_key
                # add new key to LL tail
                head_key = LL.remove_head(self.head.key)
                del curr[head_key]
                curr[key] = LinkedNode(key, value)