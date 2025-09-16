#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        idx = -1

        for num in nums:
            curr = num

            while idx != -1:
                gcd = math.gcd(nums[idx], curr)

                if gcd == 1:
                    break

                curr = nums[idx] * curr // gcd
                idx -= 1

            idx += 1
            nums[idx] = curr

        return nums[:idx+1]
