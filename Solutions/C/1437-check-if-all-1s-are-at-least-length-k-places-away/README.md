**Check If All 1's Are at Least Length K Places Away**
=
[Problem Link](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description)

## Intuition
First, find the index of the first `1` in `nums`. Then start searching from that index `start`, and count 
the current distance between `1`s. If a distance is less than `k`, return `False`.

## Approach
**Step-by-Step Process**

1. Find the index `start` of the first `1` in `nums`.
    - If not exist, return `True`.

2. Initialize the current distance of `1`s as `curr`, and search from the index `start + 1`.

3. If next `1` is found but `curr` is less than `k`, then return `False`.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        
        start = nums.index(1)
        curr = 0

        for num in nums[start+1:]:
            if num == 0:
                curr += 1

            else:
                if curr < k:
                    return False

                curr = 0

        return True
```
