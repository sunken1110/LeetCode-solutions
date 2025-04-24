#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        distinct = set(nums)
        curr = defaultdict(int)
        cnt = 0

        for right in range(n):
            curr[nums[right]] += 1

            while len(curr) == len(distinct):
                cnt += n-right
                curr[nums[left]] -= 1

                if curr[nums[left]] == 0:
                    del curr[nums[left]]

                left += 1

        return cnt
