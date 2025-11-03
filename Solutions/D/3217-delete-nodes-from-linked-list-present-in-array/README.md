**Delete Nodes From Linked List Present in Array**
=
[Problem Link](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description)

## Intuition
Remove all nodes from the given linked list whose values appears in `nums`.

## Approach
**Step-by-Step Process**

1. Initialize a set `check` to efficiently check target removal nodes.

2. Move to the first node which is not a target.

3. If the next node `curr.next` is in `check`, change the header to the `curr.next.next`.
    - In-place apparoach is applied.

4. Return updated `head`.
  
## Solutions
```python
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
```
