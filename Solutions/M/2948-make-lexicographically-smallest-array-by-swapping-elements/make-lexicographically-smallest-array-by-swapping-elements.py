#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        sub_idx = []
        sorted_idx = []
        ans = [0] * len(nums)

        prev = 0
        for val, idx in sorted_nums:
            if val > prev + limit:
                sorted_idx.extend(sorted(sub_idx))
                sub_idx = [idx]

            else:
                sub_idx += [idx]

            prev = val

        sorted_idx.extend(sorted(sub_idx))

        for new_idx, idx in enumerate(sorted_idx):
            ans[idx] = sorted_nums[new_idx][0]

        return ans
