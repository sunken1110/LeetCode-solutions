#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/24-game/description

# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6


        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < eps

            n = len(nums)

            for i in range(n):
                for j in range(i+1, n):
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = []
                    candidates.append(a+b)
                    candidates.append(a-b)
                    candidates.append(b-a)
                    candidates.append(a*b)

                    if abs(a) > eps:
                        candidates.append(b/a)

                    if abs(b) > eps:
                        candidates.append(a/b)

                    for new_num in candidates:
                        if backtrack(next_nums + [new_num]):
                            return True

            return False

        
        return backtrack([float(num) for num in cards])
