class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.data_store = {}
        self.head = None
        self.tail = None
    
    def print(self, head):
        curr = head
        while curr:
            print(f"{curr.key}-{curr.val}", end="->")
            curr = curr.next
        print()

    def get(self, key: int) -> int:
        if not key in self.data_store:
            return -1
        node = self.data_store[key]
        if self.tail == node:
            return node.val
        node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = self.head.next
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data_store:
            node = self.data_store[key]
            node.val = value
            if self.tail == node:
                return
            node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = self.head.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            return
        if self.current_size == self.capacity:
            head_node = self.head
            self.data_store.pop(head_node.key)
            self.head = head_node.next
            if not self.head:
                self.tail = None
            else:
                self.head.prev = None
            self.current_size -= 1
        new_node = ListNode(key, value)
        if not self.head and not self.tail:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.data_store[key] = new_node
        self.current_size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)