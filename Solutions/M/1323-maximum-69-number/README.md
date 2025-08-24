**Maximum 69 Number**
=
[Problem Link](https://leetcode.com/problems/maximum-69-number/description)

## Intuition
Simply find the first `6` and then replace it to `9`.

## Approach
**Step-by-Step Process**

1. Find `6` and then replace it to `9`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = list(str(num))

        for i in range(len(ans)):
            if ans[i] == '6':
                ans[i] = '9'

                return int(''.join(ans))

        return int(''.join(ans))
```
