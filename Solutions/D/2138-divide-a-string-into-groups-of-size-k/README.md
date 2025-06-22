**Divide a String Into Groups of Size K**
=
[Problem Link](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description)

## Intuition
The task is simply to add a padding `fill` to make the length of `s` a multiple of `k`.

## Approach
**Step-by-Step Process**

1. Use `divmod` to find a quotient `q` and a remainder `r` of `len(s)` divide by `k`.

2. Split `q` first length `k` strings.

3. If `r` is not a zero, pad `k-r` `fills`s to the last string.

## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        q, r = divmod(len(s), k)
        ans = [''] * q

        for i in range(q):
            ans[i] = s[i*k:(i+1)*k]

        if r > 0:
            ans.append(s[-r:])
            ans[-1] += fill * (k-r)

        return ans
```
