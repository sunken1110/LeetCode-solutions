#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-the-number-of-good-subarrays/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        left = 0
        cnt = 0
        ans = 0

        for right in range(n):
            cnt += freq[nums[right]]
            freq[nums[right]] += 1

            while cnt >= k:
                ans += n-right
                freq[nums[left]] -= 1
                cnt -= freq[nums[left]]
                left += 1

        return ans
