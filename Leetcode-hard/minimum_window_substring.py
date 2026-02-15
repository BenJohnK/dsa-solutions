from collections import defaultdict


class solution:
    def minWindowSubstring(self, s: str, t: str) -> str:
        count_dict = defaultdict(int)
        for ch in t:
            count_dict[ch] += 1
        formed = 0
        total = len(count_dict)
        left, right = 0,0
        left_index, right_index = 0,0
        len_of_total = float('inf')
        
        while right < len(s):
            if s[right] in count_dict:
                count_dict[s[right]] -= 1
                if count_dict[s[right]] == 0:
                    formed += 1
            while left <= right and formed == total:
                length = right-left+1
                if length < len_of_total:
                    len_of_total = length
                    left_index = left
                    right_index = right + 1
                current_left_char = s[left]
                if current_left_char in count_dict:
                    count_dict[current_left_char] += 1
                    if count_dict[current_left_char] > 0:
                        formed -= 1
                left += 1
            right += 1
    
        return "" if left_index == 0 and right_index == 0 else s[left_index: right_index]
     

obj = solution()
print(obj.minWindowSubstring("a", "aa"))

count_dict = {"A": 2, "B": 1, "C": 1}
