**Total Characters in String After Transformations I**
=
[Problem Link](https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description)

## Intuition
Note that the length of `s` increases when there is any `z` in it. A transformation without increment is just a 
character shifting, we can easily implement it by deque structure with a frequency vector `cnt`. 
In other word, each transformation is a repetition of `pop` and `appendleft`, and if `z` exists then
increment the counter of `b`.

## Approach
**Step-by-Step Process**

1. Initialize `cnt = deque([0] * 26)` which count the frequency of each alphabet.

2. For each product, apply the following transformation.
    - Increment the counter of `by` as the same amount of the counter of `z`.
    - Pop `s` and then left-append it to `s` again. This is a simple chracter shifting.
  
## Solutions
```python
# Time Complexity O(n+t), Space Complexity O(1)
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = deque([0] * 26)
        mod = 10**9 + 7

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            cnt[0] += cnt[25] % mod
            cnt.appendleft(cnt.pop())

        return sum(cnt) % mod
```
