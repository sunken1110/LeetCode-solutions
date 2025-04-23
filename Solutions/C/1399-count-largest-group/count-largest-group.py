#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-largest-group/description

# DP - Time Complexity O(n), Space Complexity O(n)
class Solution1:
    def countLargestGroup(self, n: int) -> int:
        dp = [0] * 10**4
        digitSum = [0] * 36

        for i in range(1, n+1):
            q, r = divmod(i, 10)
            dp[i] = dp[q] + r
            digitSum[dp[i]-1] += 1

        return digitSum.count(max(digitSum))


# Brute-force - Time Complexity O(n), Space Complexity O(n)
class Solution2:
    def countLargestGroup(self, n: int) -> int:
        def digitSum(num):
            ans = 0

            while num > 0:
                ans += num % 10
                num = num // 10

            return ans

        
        freq = defaultdict(int)

        for i in range(1, n+1):
            freq[digitSum(i)] += 1

        return len([n for n in freq.keys() if freq[n] == max(freq.values())])
