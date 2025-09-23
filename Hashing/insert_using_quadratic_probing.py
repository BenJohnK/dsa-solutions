class Solution:
    def quadraticProbing(self, arr, m):
        # code here
        h_table = []
        for i in range(m):
            h_table.append(-1)
        for x in arr:
            if x in h_table:
                continue
            if -1 not in h_table:
                break
            i = 0
            position = x%m
            while(h_table[(position+(i*i))%m]) != -1:
                i += 1
            h_table[(position+(i*i))%m] = x

        return h_table
    
x = Solution()
print(x.quadraticProbing([21, 10, 33, 43], 8))