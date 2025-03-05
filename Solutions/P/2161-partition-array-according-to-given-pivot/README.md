**Partition Array According to Given Pivot**
=
[Problem Link](https://leetcode.com/problems/partition-array-according-to-given-pivot/description)

## Intuition
We scan `nums` in order with grouping which are smaller, equal, or greater than `pivot`. 

## Approach
**Step-by-Step Process**

1. Define 3 arrays `left`, `center`, and `right`.
    - Each of them stores smaller, equal, and greater `num` in `nums`, respectively.
  
2. Scan every element in `nums`, and then store it to one of 3 arrays.

3. After scanning whole `nums`, concatentate 3 arrays.

## Solutions
```python
# Complexity O(n)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        center = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)

            elif num > pivot:
                right.append(num)

            else:
                center.append(num)

        return left + center + right
