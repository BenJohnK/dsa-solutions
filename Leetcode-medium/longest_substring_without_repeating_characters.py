class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        pointer = 0 
        high = 0
        counter_dict = {}
        for i in range(len(s)):
            if s[i] in counter_dict and counter_dict[s[i]] >= pointer:
                pointer = counter_dict[s[i]] + 1
                counter_dict[s[i]] = i
                if count > high:
                    high = count
                count = (i-pointer) + 1
            else:
                count += 1
                counter_dict[s[i]] = i

        return max(count, high)