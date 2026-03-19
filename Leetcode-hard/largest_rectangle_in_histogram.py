heights = [2,1,5,6,2,3]
# Output: 10

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(len(heights)):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]]>heights[i]:
                    previous_bar_index = stack.pop()
                    previous_bar_element = heights[previous_bar_index]
                    if stack:
                        distance = i-stack[-1]-1
                        area = previous_bar_element * distance
                    else:
                        distance = i-0
                        area = previous_bar_element * distance
                    if area > max_area:
                        max_area = area
                stack.append(i)
        
        while stack:
            previous_bar_index = stack.pop()
            previous_bar_element = heights[previous_bar_index]
            if stack:
                distance = n-stack[-1]-1
                max_area = max(max_area, previous_bar_element*distance)
            else:
                max_area = max(max_area, previous_bar_element*n)
        return max_area
    
obj = Solution()
print(obj.largestRectangleArea(heights))