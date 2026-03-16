# stack problem

temperatures = [73,74,75,71,69,72,76,73]

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new_list = [0]*len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            current_value = temperatures[i]
            while stack and current_value > temperatures[stack[-1]]:
                index = stack.pop()
                new_list[index] = i-index
            stack.append(i)
        return new_list
    
obj = Solution()
print(obj.dailyTemperatures(temperatures))