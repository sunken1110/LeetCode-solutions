**Divide Array Into Equal Pairs**
=
[Problem Link](https://leetcode.com/problems/divide-array-into-equal-pairs/description)

## Intuition
The conditions assert each array to consist of exactly 2 same elements. In short, the numbers of 
each element in `nums` are even.


## Approach
**Step-by-Step Process**

1. Use `Counter` to check the frequency of each elements in `nums`.

2. Check if there is any element that the frequency is odd.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = Counter(nums)

        for freq in nums.values():
            if freq % 2 != 0:
                return False

        return True
```
