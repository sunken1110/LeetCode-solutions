#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        for dir in range(2):
            total_ops = 0
            partial_ops = 0

            if dir == 0:
                for i in range(n):
                    ans[i] += total_ops
                    partial_ops += int(boxes[i])
                    total_ops += partial_ops

            else:
                for i in range(n-1, -1, -1):
                    ans[i] += total_ops
                    partial_ops += int(boxes[i])
                    total_ops += partial_ops

        return ans


class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                ans[i] += abs(j-i) * int(boxes[j])

        return ans

