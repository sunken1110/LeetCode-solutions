**24 Game**
=
[Problem Link](https://leetcode.com/problems/24-game/description)

## Intuition
Since there are only 4 cards, there are 4! ways to place the numbers, 4^3 ways to place the operations, and 5 ways 
to place the parentheses. Since the total cases are not too large, we can check every possibilities with backtracking. 
First, pick 2 cards in `nums` then compute every possible result from 4 operations. Recurse the result to the next 
step of backtracking until no card is remained. To avoid the decimal error, we use `eps`.

## Approach
**Step-by-Step Process**

1. Construct a backtracking.
    - Pick 2 cards from `cards`.
    - Compute every possible result from 4 operations, and recurse to the next step.
    - If no card is remained, compare to 24.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6


        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < eps

            n = len(nums)

            for i in range(n):
                for j in range(i+1, n):
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = []
                    candidates.append(a+b)
                    candidates.append(a-b)
                    candidates.append(b-a)
                    candidates.append(a*b)

                    if abs(a) > eps:
                        candidates.append(b/a)

                    if abs(b) > eps:
                        candidates.append(a/b)

                    for new_num in candidates:
                        if backtrack(next_nums + [new_num]):
                            return True

            return False

        
        return backtrack([float(num) for num in cards])
```
