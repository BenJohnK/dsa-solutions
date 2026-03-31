class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data_store = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
    
    def print(self, head):
        curr = head
        while curr:
            print(f"{curr.key}-{curr.val}", end="->")
            curr = curr.next
        print()
    
    def attach_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail
    
    def move_to_tail(self, node):
        if self.tail.prev == node:
            return # do nothing because the given node itself is the tail
        
        # detach node
        node.prev.next = node.next
        node.next.prev = node.prev

        #attach to tail
        self.attach_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.data_store:
            return -1
        node = self.data_store[key]
        self.move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data_store:
            node = self.data_store[key]
            node.val = value
            self.move_to_tail(node)
            return
        if len(self.data_store) == self.capacity:
            lru = self.head.next
            self.data_store.pop(lru.key)
            self.head.next = lru.next
            lru.next.prev = self.head
        new_node = ListNode(key, value)
        self.attach_to_tail(new_node)
        self.data_store[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)