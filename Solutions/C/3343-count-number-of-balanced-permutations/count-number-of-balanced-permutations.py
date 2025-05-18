#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-number-of-balanced-permutations/description

# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        total_sum = sum(int(i) for i in num)

        if total_sum % 2 == 1:
            return 0

        odd = len(num) // 2
        even = (len(num) + 1) // 2
        half_sum = total_sum // 2
        mod = 10**9 + 7
        freq = Counter(int(i) for i in num)


        @cache
        def dfs(digit, num_odd, num_even, balance):
            if num_odd == 0 and num_even == 0 and balance == 0:
                return 1

            if digit < 0 or num_odd < 0 or num_even < 0 or balance < 0:
                return 0

            cnt = 0

            # counter of digit -> distribute to odd/even indices
            for i in range(freq[digit] + 1):
                cnt += comb(num_odd, i) * comb(num_even, freq[digit]-i) * dfs(digit-1, num_odd-i, num_even-freq[digit]+i, balance-i*digit)

            return cnt % mod

        
        return dfs(9, odd, even, half_sum)
