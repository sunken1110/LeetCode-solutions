**Count the Hidden Sequences**
=
[Problem Link](https://leetcode.com/problems/count-the-hidden-sequences/description)

## Intuition
The idea is to find a range of sequence and check if the lower and upper bounds can cover that range. 
Since we only know the differences of consecutive indices, we fix the first element as 0 and track the prefix sum. 
Suppose `prefix_min` and `prefix_max` are the lowest and highest prefix sum respectively. Once the range falls 
within the boundary, then the gap between `lower` and `prefix_min` is adjustable range to decrease each value of 
sequence by 1. Similarly, the gap between `upper` and `prefix_max` is adjustable range to increase. The answer is 
the count of available increments and decrements.

## Approach
**Step-by-Step Process**

1. Initialize `prefix`, `prefix_min` and `prefix_max` as 0.

2. With `differences`, track the current, minimal, and maximal prefix sum.

3. Calculate the possible increments and decrements within boundary between `lower` and `upper`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_min = 0
        prefix_max = 0
        prefix = 0

        for diff in differences:
            prefix += diff

            if prefix_min > prefix:
                prefix_min = prefix

            if prefix_max < prefix:
                prefix_max = prefix

        return max(0, (upper-lower) - (prefix_max-prefix_min) + 1)
