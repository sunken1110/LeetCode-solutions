**Set Intersection Size At Least Two**
=
[Problem Link](https://leetcode.com/problems/set-intersection-size-at-least-two/description)

## Intuition
We start from the smallest right index `r` of each `invertval` in `intervals`. To contain at least 2 integers 
of every `interval` with right index `r` we need to choose `r-1` and `r`; then clearly windows with much 
smaller left index also can be dealt with. That is, the first step is to sort `intervals` in ascending 
right index and descending left index. Suppose the first containing interval is defined and we want to find 
the next containing interval `[a, b]`. If current interval `[l, r]` is completely disjoint to `[a, b]`, then 
similarly `[r-1, r-2]` should be the target. If there exists an intersection, then we can use a previous `b` 
as one integer and add `r` as the other new integer, i.e., `a = b` and `b = r`. Repeat this process until 
we scan every `interval`.

## Approach
**Step-by-Step Process**

1. Initialize current containing set as `[a, b]`.

2. Sort `intervals` in the order of ascending right index and descending left index.

3. For each `[l, r]` in `intervals`, check the location of previous window `[a, b]`.
    - If `l > b`, two windows are completely disjoint; take two largest integer `r-1` and `r`.
    - Elif `a < l <= b`, take `r` as an additional integer.

4. Return the size of containing set.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1
        ans = 0

        for l, r in intervals:
            if l > b:
                a = r-1
                b = r
                ans += 2

            elif l > a:
                a = b
                b = r
                ans += 1

        return ans
```
