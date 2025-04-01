#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/solving-questions-with-brainpower/description

# Complexity O(n)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            if i + questions[i][1] + 1 < n:
                dp[i] = max(dp[i+1], questions[i][0] + dp[i+questions[i][1] + 1])

            else:
                dp[i] = max(dp[i+1], questions[i][0])

        return dp[0]
