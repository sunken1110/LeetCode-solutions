**Delete Columns to Make Sorted**
=
[Problem Link](https://leetcode.com/problems/delete-columns-to-make-sorted/description)

## Intuition
We simply collect every `i`th character of every strings in `strs`, namely `col`. Then we check if `col` 
is already sorted or not.

## Approach
**Step-by-Step Process**

1. Use `zip` to collect each `i`th character of every strings in `strs`.
    - Denote it as `col`.

2. If `col` is already sorted, then count 1.
  
## Solutions
```python
# Time Complexity O(mn*log(n)), Space Complexity O(n)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0

        for col in zip(*strs):
            if list(col) != sorted(col):
                cnt += 1

        return cnt
```
