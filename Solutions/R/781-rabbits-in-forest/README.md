**Rabbits in Forest**
=
[Problem Link](https://leetcode.com/problems/rabbits-in-forest/description)

## Intuition
Suppose there are `cnt` rabbits that answered the number of same colored rabbits are `val`. To minimize the total 
number of rabbits, we first partition `cnt` into `val+1`. Here, `val+1` includes the answered rabbit itself. 
If `cnt % (val+1)` is not zero, then there exists other rabbits in forest that isn't included in initial questioning. 
Then the minimum number of groups of `cnt` rabbits are `ceil(val // (val+1))`, and the answer is a sum of them.

## Approach
**Step-by-Step Process**

1. For an easy count for same colored rabbits, we use `Counter`.

2. For each groups, calculate the minimum number of groups.
    - Since each group must be fully grouped, the total number of rabbits is a multiple by `val+1`.

4. Sum them up.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        ans = 0

        for val, cnt in freq.items():
            ans += (cnt+val) // (val+1) * (val+1)

        return ans
