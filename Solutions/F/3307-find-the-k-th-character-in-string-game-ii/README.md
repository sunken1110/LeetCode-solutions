**Find the K-th Character in String Game II**
=
[Problem Link](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description)

## Intuition
The problem is a tricky version of the following:

[Problem Link](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description)

Since the length of word increases double for each step, the origin of `k`th letter can be found by reversely 
tracing the bit of `k`.

## Approach
**Step-by-Step Process**

1. Initialize `shifts` the number of changing operations of `k`th letter.

2. For each digit, calculate `1 << digit` and subtract from `k`.
    - If `1 << digit` equals `k`, then move to the previous bit-block, ie., `digit -= 1`.
  
3. If changing operations worked, then add 1 to `shifts`.
  
## Solutions
```python
# Time Complexity O(log(k)), Space Complexity O(1)
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shifts = 0

        while k != 1:
            digit = k.bit_length() - 1

            if (1 << digit) == k:
                digit -= 1

            k -= (1 << digit)

            if operations[digit]:
                shifts += 1

        return chr((shifts % 26) + ord('a'))
```
