#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description

# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        parent = '-'
        ans = []

        for f in folder:
            if parent + '/' in f and f.startswith(parent):
                continue

            else:
                parent = f
                ans.append(parent)

        return ans
