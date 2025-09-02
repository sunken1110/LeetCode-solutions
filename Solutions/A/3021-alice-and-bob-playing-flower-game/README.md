**Alice and Bob Playing Flower Game**
=
[Problem Link](https://leetcode.com/problems/alice-and-bob-playing-flower-game/description)

## Intuition
Note that the game result of `(x, y)` is same to `(x+2, y)` and `(x, y+2)` since Alice and Bob take turns. 
Then the winning condition is equivalent to if `(x, y)` can be transformed to either `(2, 1)` or `(1, 2)`, since Alice 
starts the game first. In short, if `x` is odd then `y` should be even and vice versa. Then the problem is simply 
to count the number of pairs that `(x, y)` is odd-even or even-odd in the range `[1, n]`, `[1, m]`, which is 
`(m*n) // 2`

## Approach
**Step-by-Step Process**

1. According to the above discussion, compute the number of valid pairs.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m*n) // 2
```
