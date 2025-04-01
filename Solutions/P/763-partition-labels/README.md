**Partition Labels**
=
[Problem Link](https://leetcode.com/problems/partition-labels/description)

## Intuition
At the first scanning, we check each alphabet's last occurrence. At the second scanning, we check two pointers of 
current index and the maximal index of scanned alphabets. If two coincides, then the word before it can be 
partitioned.

## Approach
**Step-by-Step Process**

1. Initialize each alphabet's last index `last_idx` as -1.
  
2. Complete `last_idx` with the first scan.

3. For the second scan, track the maximum of `last_idx` of scanned alphabet.
    - If the index of scanned alphabet and `max(last_idx)` are the same, then partition it.

## Solutions
```python
# Complexity O(n)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_idx = [-1] * 26
        ans = []

        for idx, char in enumerate(s):
            alphabet = ord(char) - ord('a')
            last_idx[alphabet] = idx

        left = 0
        right = -1

        for idx, char in enumerate(s):
            alphabet = ord(char) - ord('a')
            right = max(right, last_idx[alphabet])

            if idx == right:
                ans.append(right - left + 1)
                left = idx + 1

        return ans
