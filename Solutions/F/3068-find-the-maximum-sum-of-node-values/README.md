**Find the Maximum Sum of Node Values**
=
[Problem Link](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description)

## Intuition
The critical idea is that double XOR is an identity. Since it is a undirected tree, every node can be connected
by a path, let's say 'x-a-b-c-y'. Do XOR for every edge results: 2 XOR for a, b, c and 1 XOR for x, y, which 
coincides to a single XOR of x-y as they are directly connected. Now, we greedily check every node's surplus of the 
original value and the XORed value. Since each operation flips the values of 2 nodes, we sort the surplus and pick 
positive surplus pairs only.

## Approach
**Step-by-Step Process**

1. Visit every node.
    - Add every value of `num` in `nums`.
    - Store the difference of `num` and `num` XOR `k` to `xor_diff`.

2. Sort `xor_diff` in descending order.

3. Add the first two differences of `xor_diff` until the gap is positive.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0
        xor_diff = []

        for num in nums:
            ans += num
            xor = num ^ k
            xor_diff.append(xor - num)

        xor_diff.sort(reverse=True)

        for i in range(0, len(xor_diff)-1, 2):
            if xor_diff[i] + xor_diff[i+1] <= 0:
                break

            ans += xor_diff[i] + xor_diff[i+1]

        return ans
```
