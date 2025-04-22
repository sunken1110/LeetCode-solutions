#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description

# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        ans = []

        for idx, size in enumerate(groupSizes):
            groups[size].append(idx)

            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = []

        return ans
