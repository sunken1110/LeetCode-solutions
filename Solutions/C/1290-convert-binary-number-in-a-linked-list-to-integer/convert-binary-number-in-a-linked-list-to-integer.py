#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description

# Time Complexity O(n), Space Complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0

        while head:
            ans = 2*ans + head.val
            head = head.next

        return ans
