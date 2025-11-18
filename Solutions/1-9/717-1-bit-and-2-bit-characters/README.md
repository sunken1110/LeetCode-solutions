**1-bit and 2-bit Characters**
=
[Problem Link](https://leetcode.com/problems/1-bit-and-2-bit-characters/description)

## Intuition
We remove characters in order; if a previous character is `1` then the next character must be removed simultaneously. 
If we removed every character and the last previous character is `1`, then the last character must be two-bit 
character `10` or `11`.

## Approach
**Step-by-Step Process**

1. Initialize a previous character `prev` as `-1`.

2. For `bit` in `bits`, update `prev` while removing each `1`.

3. If the last previous character is `0`, return `True`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        prev = -1

        for bit in bits:
            if prev == 1:
                prev = -1
                continue

            prev = bit

        return prev == 0
```
