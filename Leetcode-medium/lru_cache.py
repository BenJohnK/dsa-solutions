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
        self.head = None
        self.tail = None
    
    def print(self, head):
        curr = head
        while curr:
            print(f"{curr.key}-{curr.val}", end="->")
            curr = curr.next
        print()
    
    def move_to_tail(self, node):
        if not node.next:
            return # do nothing because the given node itself is the tail
        if not node.prev:
            self.head = node.next # means current node is head. so move head to node.next
        else:
            node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node # moved the node to tail

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
            head_node = self.head
            self.data_store.pop(head_node.key)
            self.head = head_node.next
            if not self.head:
                self.tail = None
            else:
                self.head.prev = None
        new_node = ListNode(key, value)
        if not self.head and not self.tail:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.data_store[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)