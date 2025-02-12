#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description

# Complexity O(n*log(n))
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_set = defaultdict(list)
        max_sum = -1

        nums.sort(reverse=True)

        def digitSum(x):
            s = 0

            while x > 0:
                s += x % 10
                x = x // 10

            return s

        for num in nums:
            digit_sum = digitSum(num)

            if len(sum_set[digit_sum]) <= 1:
                sum_set[digit_sum].append(num)

        for num_list in sum_set.values():
            if len(num_list) == 2:
                max_sum = max(max_sum, sum(num_list))

        return max_sum
