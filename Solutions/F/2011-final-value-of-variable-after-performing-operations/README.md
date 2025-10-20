**Final Value of Variable After Performing Operations**
=
[Problem Link](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description)

## Intuition
For each `op` in `operations`, if `++` is contained then get +1, else -1. 

## Approach
**Step-by-Step Process**

1. Initialize `cnt`.

2. For each `op` in `operations`, check if `++` or `--` is contained.
    - If `++`, `cnt += 1`.
    - Else, `cnt -= 1`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cnt = 0

        for op in operations:
            if '++' in op:
                cnt += 1

            else:
                cnt -= 1

        return cnt
```
