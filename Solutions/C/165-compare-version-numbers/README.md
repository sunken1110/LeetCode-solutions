**Compare Version Numbers**
=
[Problem Link](https://leetcode.com/problems/compare-version-numbers/description)

## Intuition
We split two strings based on '.' and compare each of them. To maintain the order condition, we denote each 
partition as an integer; for example, '001' = 0 * 10^2 + 0 * 10^1 + 1 * 10^0.

## Approach
**Step-by-Step Process**

1. Split two strings based on '.'.

2. For each partitions, transfer to two integers `num1` and `num2`.

3. Compare `num1` and `num2` until they are different.
    - If no difference occurred, then return 0.
  
## Solutions
```python
# Time Complexity O(m+n), Space Complexity O(1)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        m, n = len(version1), len(version2)

        while i < m or j < n:
            num1, num2 = 0, 0

            while i < m and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1

            while j < n and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1

            if num1 > num2:
                return 1

            elif num1 < num2:
                return -1

            if i < m and version1[i] == '.':
                i += 1

            if j < n and version2[j] == '.':
                j += 1

        return 0
```
