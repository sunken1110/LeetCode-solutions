**Find Lucky Integer in an Array**
=
[Problem Link](https://leetcode.com/problems/find-lucky-integer-in-an-array/description)

## Intuition
Use `Counter` to count the frequency of each integer in `arr`. Then return the maximal integer such that the 
frequency is equal to its value.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count the frequency `freq` of each integer in `arr`.

2. Initialize a `lucky` as `-1`.

3. For each item in `freq`, check if the value is equal to its frequency.
    - If so, update `lucky` if it is larger than the previously found lucky integer.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = -1

        for num, val in freq.items():
            if num == val:
                lucky = max(lucky, num)

        return lucky
```
