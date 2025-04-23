#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-good-triplets-in-an-array/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        class BIT:
            def __init__(self, n):
                self.tree = [0] * (n+1)

            def update(self, idx, x):
                idx += 1
                
                while idx < n+1:
                    self.tree[idx] += x
                    idx += (idx & -idx)

            def query(self, idx):
                idx += 1
                cnt = 0

                while idx > 0:
                    cnt += self.tree[idx]
                    idx -= (idx & -idx)

                return cnt


        n = len(nums1)
        bit = BIT(n)
        cnt = 0
        mapping = {val: idx for idx, val in enumerate(nums1)}

        for num in nums2:
            idx = mapping[num]
            left = bit.query(idx)
            right = (n-1-idx) - (bit.query(n-1)-left)
            cnt += left * right
            bit.update(idx, 1)

        return cnt