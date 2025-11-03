#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description

# Time Complexity O(n+h), Space Complexity O(n+h)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        check = set(nums)

        while head and head.val in check:
            head = head.next

        curr = head

        while curr and curr.next:
            if curr.next.val in check:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head
