# class cache:
#     def __init__(self, capacity):
#         self.memo = {}
#         self.capacity = capacity
#     def insert(self, key, val):
#         curr = self.memo
#         if key in curr:
#             del curr[key]
#             print(curr)
#             curr[key] = val # updates original val to new val
#             print(curr)
#         else:
#             curr[key] = val
#             print(curr)

#     def get(self, key):
#         curr = self.memo
#         try:
#             temp = curr[key]
#             print(temp)
#         except KeyError as e:
#             print("key not in cache", e) 

class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = prev

class cache:
    def __init__(self, capacity):
        self.memo = {}
        self.capacity = capacity
        self.dummy = LinkedNode(0,0)
        self.head = self.dummy.next
        self.tail = self.dummy.next

    def removeHeadNode(self):
        if self.head is None:               # Check if head is empty
            return  
        else:                       
            temp = self.head
            self.head = self.head.next      # Nothing to the left, but possibly something to the right
            if self.head:
                self.head.prev = None       # If head, make the head left == None
            del temp                        # Delete old head


    def addNodeLL(self, node):
        if self.tail is None:                   # If tail is empty, it means head is empty as well becaue first node appended is head and tail
            self.head = self.tail = node
        else:
            self.tail.next = node               # Add to tail
            node.prev = self.tail               # Double LL, so link both directions
            self.tail = self.tail.next          # After linking new node to LL, the new_node now bbecomes tail node or (MRU) node

    def unlinkNode(self, node):                 # Removes node from LL
        if node is self.head:                   # If node == head:
            self.head = node.next               # 1. Make self.head next node in LL
            if node.next:                       # If that worked
                node.next.prev = None           # 2. Remove the curr head
        else:
            prev, next = node.prev, node.next   # Else, the left (next) and right (prev) of node to remove   
            prev.next = next                    # Left == Right
            next.prev = prev                    # and Right == Left, essentially removing the node in the middle

    def get(self, key):
        curr = self.memo
        if key not in curr:                     # 1. Check if in memo, if not return
            return "Key not in cache"
        node = curr[key]
        if node != self.tail:                   # 2. Check if node == tail, if yes return value, as no need to unlink from queue
            self.unlinkNode(node)
            self.addNodeLL(node)
        print(node.val)
        return node.val

    def put(self, key, val):        # Insert
        curr = self.memo            
        if key in curr:                     # 1. Check if key in cache, if yes, update value and call get
            curr[key].val = val     
            self.get(key)
            return
        else:
            if len(self.memo) == self.capacity:  # If at capacity remove head from 1. Cache, 2. LL
                del curr[self.head.key]     # Remove old head from cache
                self.removeHeadNode()        # Remove old head from LL
            node = LinkedNode(key, val)     # Now create new node to add to 1. Cache, 2. LL
            curr[key] = node                # 1. Cache
            self.addNodeLL(node)            # 2. Add to LL


Run = cache(1)
Run.put(2, 1)
Run.get(2)
# Run.put("a", 100)
# Run.put("a", 200)
# Run.get(1000)
