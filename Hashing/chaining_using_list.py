class MyHash:
    def __init__(self, number_of_keys):
        self.bucket_list = []
        self.BUCKET = number_of_keys
        for i in range(number_of_keys):
            self.bucket_list.append([])
    
    def insert(self, key):
        position_to_be_inserted = key % self.BUCKET
        self.bucket_list[position_to_be_inserted].append(key)
        return "inserted"
    
    def search(self, key):
        position = key % self.BUCKET
        if key in self.bucket_list[position]:
            return True
        else:
            return False
    
    def delete(self, key):
        position = key % self.BUCKET
        if key in self.bucket_list[position]:
            self.bucket_list[position].remove(key)
            return "removed"
        return "removed"


h=MyHash(7)
print(h.insert(70))
print(h.insert(60))
print(h.insert(140))
print(h.search(60))
print(h.delete(60))
print(h.search(60))
print(h.bucket_list)
