class Solution:
    def linearProbing(self, arr, m):
        #code here
        my_hash_table = []
        for i in range(m):
            my_hash_table.append(-1)
        for x in arr:
            position = x%m
            inserted = False
            for i in range(position, m):
                if my_hash_table[i] == x:
                    inserted = True
                    break
                if my_hash_table[i] == -1:
                    my_hash_table[i] = x
                    inserted = True
                    break
            if not inserted:
                for i in range(0, position):
                    if my_hash_table[i] == x:
                        break
                    if my_hash_table[i] == -1:
                        my_hash_table[i] = x
                        break
        return my_hash_table

x = Solution()
print(x.linearProbing([3,11,10], 3))