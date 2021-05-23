# Leetcode 146. LRU Cache

# 1. Create Dummy node, and set head and tail to dummy.next
# 2. 

# When a get request is made for value already in cache, that value needs to be unlinked
# and repopulated as newest element in LL as this was the latest element requested.



class LinkedNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memo = {}
        self.dummy = LinkedNode(0,0)
        self.head = self.dummy.next
        self.tail = self.dummy.next
        
    def remove_head_node(self):
        if not self.head:
            return
        prev = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del prev
        
    def append_new_node(self, new_node):
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
    
    def unlink_curr_node(self, node):
        if self.head is node:
            self.head = node.next
            if node.next:
                node.next.prev = None
            return
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev
            
    def get(self, key):
        if key not in self.memo:
            return -1
        node = self.memo[key]
        if node is not self.tail:
            self.unlink_curr_node(node)
            self.append_new_node(node)
        return node.val

    def put(self, key, value):
        if key in self.memo:
            self.memo[key].val = value
            self.get(key)
            return
        if len(self.memo) == self.capacity:
            self.memo.pop(self.head.key)
            self.remove_head_node()
        
        new_node = LinkedNode(val=value, key=key)
        self.memo[key] = new_node
        self.append_new_node(new_node)
        
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2,2)
param_3 = obj.get(1)
print(param_3)
obj.put(3,3)
param_3 = obj.get(2)
print(param_3)
