#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description

# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        freq = Counter(nums[:k])

        for i in range(n-k+1):
            sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
            top_x = set(num for num, _ in sorted_freq[:x])
            x_sum = 0

            for num in top_x:
                x_sum += num * freq[num]

            ans.append(x_sum)

            if i + k < n:
                freq[nums[i]] -= 1
                freq[nums[i+k]] += 1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]

        return ans
