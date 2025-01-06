#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

# Linear Scanning - Complexity O(n)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        for direction in range(2):
            total_ops = 0    # Cumulative sum of ops
            partial_ops = 0    # Ops for ith box to (i+1)th box, where already 0 ~ (i-1)th boxes are moved to ith (left -> right case)

            # left -> right scanning
            if direction == 0:
                for i in range(n):
                    ans[i] += total_ops
                    partial_ops += int(boxes[i])
                    total_ops += partial_ops

            # right -> left scanning
            else:
                for i in range(n-1, -1, -1):
                    ans[i] += total_ops
                    partial_ops += int(boxes[i])
                    total_ops += partial_ops

        return ans

# Brute Force - Complexity O(n^2)
class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                ans[i] += abs(j-i) * int(boxes[j])

        return ans

