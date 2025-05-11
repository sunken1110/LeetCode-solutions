**Minimum Equal Sum of Two Arrays After Replacing Zeros**
=
[Problem Link](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description)

## Intuition
Since every 0 in both `nums1` and `nums2` should be replaced at least by 1, it should be considered as 1 for 
computing the total sum. Since 0 can be replaced to every positive number, what we have to check is if the list 
with more smaller total sum has 0 or not.

## Approach
**Step-by-Step Process**

1. Count zeroes of `nums1` and `nums2`.

2. Compute the minimum total sum after replacement of `nums1` and `nums2`.

3. Check if the list with smaller sum has 0 or not.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        sum1 = sum(nums1) + zero1
        sum2 = sum(nums2) + zero2

        if (sum1 > sum2 and zero2 == 0) or (sum1 < sum2 and zero1 == 0):
            return -1

        return max(sum1, sum2)
```
