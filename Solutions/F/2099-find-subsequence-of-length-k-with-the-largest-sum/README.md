**Find Subsequence of Length K With the Largest Sum**
=
[Problem Link](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description)

## Intuition
A required subsequence allows to delete other element, so what we need is to find `k` most largest elements. 
Sort `nums` and find the largest `k` elements, and then return them in the original order.

## Approach
**Step-by-Step Process**

1. Sort `nums`.

2. Return the `k` most largest numbers of sorted `nums` in the original order.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))

        return [num for num, _ in sorted(sorted_nums[-k:], key=lambda x: x[1])]
```
