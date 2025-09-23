class MyHash:
    def __init__(self, size):
        self.h_table = []
        self.table_size = size
        for i in range(size):
            self.h_table.append(None)
    
    def insert(self, value):
        if None not in self.h_table and "deleted" not in self.h_table:
            return "full"
        if value in self.h_table:
            return "Already present"
        position = value % self.table_size
        i = 0
        while self.h_table[(position + i)%self.table_size] != None and self.h_table[(position + i)%self.table_size] != "deleted":
             i += 1
        self.h_table[(position + i)%self.table_size] = value
        return "Inserted"
    
    def search(self, value):
        position = value % self.table_size
        i = 0
        while self.h_table[(position + i)%self.table_size] != value and self.h_table[(position + i)%self.table_size] != "None":
            i += 1
            if (position + i) % self.table_size == position:
                return False
        if self.h_table[(position + i)%self.table_size] == value:
            return True
        return False

    def delete(self, value):
        position = value % self.table_size
        i = 0
        while self.h_table[(position + i)%self.table_size] != value and self.h_table[(position + i)%self.table_size] != "None":
            i += 1
            if (position + i) % self.table_size == position:
                return "Element is not present"
        if self.h_table[(position + i)%self.table_size] == value:
            self.h_table[(position + i)%self.table_size] = "deleted"
            return "Element is deleted"
        return "Element is not present"


h=MyHash(7)
print(h.insert(49))
print(h.insert(56))
print(h.insert(72))
print(h.search(56))
print(h.h_table)
print(h.delete(56))
print(h.search(56))
print(h.h_table)
print(h.insert(70))
print(h.h_table)
print(h.insert(70))
print(h.insert(73))
print(h.insert(74))
print(h.insert(75))
print(h.insert(76))
print(h.h_table)
print(h.insert(76))
print(h.search(83))
print(h.delete(76))
print(h.h_table)
print(h.insert(83))
print(h.h_table)
print(h.search(83))