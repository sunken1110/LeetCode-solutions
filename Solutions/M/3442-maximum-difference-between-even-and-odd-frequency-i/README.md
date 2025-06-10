**Maximum Difference Between Even and Odd Frequency I**
=
[Problem Link](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description)

## Intuition
Since strings with odd frequency and strings with even frequency are independent, the maximum difference occurs when 
`freq(a1)` is maximized and `freq(a2)` is minimized.

## Approach
**Step-by-Step Process**

1. Use `Counter` to check the frequency `freq` is odd or even.

2. Check all items in `freq`
    - Update `max_odd` and `min_even`, the maximum odd frequency and minimum even frequency, respectively.
  
## Solutions
```python
# Time Complexity O(n), Space Complexityt O(n)
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = 0
        min_even = inf

        for char, cnt in freq.items():
            if cnt % 2 == 0:
                min_even = min(min_even, cnt)

            else:
                max_odd = max(max_odd, cnt)

        return max_odd - min_even
```
