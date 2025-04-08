**Sum of All Subset XOR Totals**
=
[Problem Link](https://leetcode.com/problems/sum-of-all-subset-xor-totals/description)

## Intuition
The task requires to check all subset of given array, so DFS with backtracking is a good approach. In the sense of 
each `num` in `nums`, there are 2 possibilities that contained or not contained in a subset which leads to  
totally `2**len(nums)` subsets. Then in each backtrack step we can branch into 2 ways, select the current `num` or not.

## Approach
**Step-by-Step Process**

1. Define a backtracking with the current index `i` and cumulative sum `curr`.

2. If backtracking visited all indices, then add the current sum to total.

3. Backtrack to both `i + 1` with `curr` and `curr ^ nums[i]`.
  
## Solutions
```python
# Time Complexity O(2^n), Space Complexity O(n)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0


        def backtrack(i, curr):
            if i == len(nums):
                self.ans += curr
                return

            backtrack(i + 1, curr)
            backtrack(i + 1, curr ^ nums[i])

        
        backtrack(0, 0)

        return self.ans
```
