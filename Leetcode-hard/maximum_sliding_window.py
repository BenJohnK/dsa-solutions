nums = [1]
k = 0

# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# nums = [1,2,3] # 1 < n < 10^5
# # deque = []
# k = 1

from collections import deque

def maxSlidingWindow(nums: list, k: int) -> list:
    n = len(nums)
    max_window_list = []
    m_deque = deque()
    for right in range(n):
        if m_deque and right-k+1 > m_deque[0]:
            m_deque.popleft()
        element = nums[right]
        while m_deque and nums[m_deque[-1]] < element:
            m_deque.pop()
        m_deque.append(right)
        if right >= k-1: 
            max_window_list.append(nums[m_deque[0]])
    return max_window_list

print(maxSlidingWindow(nums, k))