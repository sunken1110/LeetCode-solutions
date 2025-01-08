**Minimum Number of Operations to Move All Balls to Each Box**
=
[Problem Link](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description)

## Intuition
To configure the total number of operations for each box, we have to scan all other boxes. Notice that, for the case of ith box,

1. `ans[i]` is the sum of total number of operations from left-side (0 ~ i-1th) and right-side (i+1 ~ nth).

2. If we assume every left-side balls are already moved to (i-1)th box, then the left-side sum of `ans[i]` is the number of balls
    in (i-1)th box since each operations allow exactly 1 move to the adjacent boxes.

Now we store a cumulative sum `partial_ops` for moving every left-side ball to (i-1)th box while linear scanning from left to right
and vice versa, to return `ans`.

## Approach
**Step-by-Step Process**

1. Store a cumulative sum `partial_ops` of (i-1)th box while traversing.

2. Check if (i-1)th box is empty or not and add it to get `total_ops` of ith box.

3. Repeat the other direction traversing.
  
## Solutions
```python
# Linear Scanning - Complexity O(n)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        for direction in range(2):
            total_ops = 0
            partial_ops = 0

            if direction == 0:
                for i in range(n):
                    ans[i] += total_ops
                    partial_ops += int(boxes[i])
                    total_ops += partial_ops

            else:
                for i in range(n-1 , -1, -1):
                    ans[i] += total_ops
                    partial_ops += int(boxes[i])
                    total_ops += partial_ops

        return ans


# Brute-force - Complexity O(n^2)
class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                ans[i] += abs(j-i) * int(boxes[j])

        return ans
```
