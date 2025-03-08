**Minimum Recolors to Get K Consecutive Black Blocks**
=
[Problem Link](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description)

## Intuition
Since we need k consecutive black blocks, it is enough to check n-k-1 substrings of length k in `blocks`. 
In this case, sliding window is appropriate. Suppose we know the required number of operations 
for a fixed block `blocks[i:i+k]`. Then the required number of operations for `blocks[i+1:i+k+1]` can be 
determined by `blocks[i] == 'B'` and `blocks[i+k+1] == 'B'`. 

## Approach
**Step-by-Step Process**

1. Check the first window `blocks[0:k]`.
    - Required operations is the total number of 'W's. Initialize the global minimum `min_ops` and `ops`.

2. Move to the next window, then compute new `ops`.
    - If `block[i] == 'B'`, then it doesn't affect to required ops of `blocks[i+1:i+k+1]`.
    - If `block[i+k+1] == 'B'`, then it doesn't affect to required ops of `blocks[i+1:i+k+1]`.

3. Apply sliding window technique to find `min_ops`.

   
## Solutions
```python
# Complexity O(n)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        consec = blocks[0:k]
        min_ops = ops = consec.count('W')

        for i in range(n-k):
            left = 0 if blocks[i] == 'B' else 1
            right = 0 if blocks[i+k] == 'B' else 1

            ops += right - left
            min_ops = min(min_ops, ops)

        return min_ops
```
