**Taking Maximum Energy From the Mystic Dungeon**
=
[Problem Link](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description)

## Intuition
Since a teleport allows excatly `k` jumps, we can partition by modulo `k`. For each partition, the maximum energy 
can be obtained by select a proper starting point. To do it, we need every cumulative sum of each starting point. 
That is, for an efficiency, we can use suffix sum for each points. Reverse the order of `energy`, and compute the 
partial suffix sum of each partition as `energy[i]` = `energy[i] + energy[i-k]`. The resulted `energy` is the 
maximum of it.

## Approach
**Step-by-Step Process**

1. Initialize `suffix_sum` by reversing `energy`.

2. Compute the suffix sum as `suffix_sum[i] += suffix_sum[i-k]`.

3. Return the maximum value of `suffix_sum`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        suffix_sum = energy[::-1]

        for i in range(k, n):
            suffix_sum[i] += suffix_sum[i-k]

        return max(suffix_sum)
```
