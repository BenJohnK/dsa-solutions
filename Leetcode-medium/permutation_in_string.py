from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_dict = defaultdict(int)
        for ch in s1:
            counter_dict[ch] += 1
        l,r = 0,0
        formed = 0
        total = len(counter_dict)

        while r < len(s2):
            if ((r-l) + 1) > len(s1):
                left_char = s2[l]
                if left_char in counter_dict:
                    counter_dict[left_char] += 1
                    if counter_dict[left_char] == 1:
                        formed -= 1
                l += 1
            char = s2[r]
            if char in counter_dict:
                counter_dict[char] -= 1
                if counter_dict[char] == 0:
                    formed += 1
                if formed == total:
                    return True
            else:
                while l<r:
                    current_left_char = s2[l]
                    if current_left_char in counter_dict:
                        counter_dict[current_left_char] += 1
                        if counter_dict[current_left_char] == 1:
                            formed -= 1
                    l += 1
                l += 1

            r += 1
        
        return False

obj = Solution()
print(obj.checkInclusion("abc", "cabd"))

# d = {a: 0,
#      b: -1,
#      c: 1}

# formed = 2
# total = 3