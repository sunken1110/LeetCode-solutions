**Convert Binary Number in a Linked List to Integer**
=
[Problem Link](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description)

## Intuition
Naive approach is enough.

## Approach
**Step-by-Step Process**

1. Initialize `ans` and start from the most significant bit `head.val`, sum it to `ans`.

2. Move to the next significant bit `head,next`, and then double `ans`.

3. Repeat until we meet the tail of a linked list.
  
## Solutions
```python
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
```
