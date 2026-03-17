nums1 = [2,4] 
nums2 = [1,2,3,4]
# Output: [3,-1]

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        helper_dict = {}
        ans = []
        for i in range(len(nums2)):
            current_element = nums2[i]
            helper_dict[current_element] = -1
            while stack and nums2[stack[-1]] < current_element:
                index = stack.pop()
                helper_dict[nums2[index]] = current_element
            stack.append(i)
        for num in nums1:
            ans.append(helper_dict[num])
        print(helper_dict)
        return ans
    

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))