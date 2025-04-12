**Count the Number of Powerful Integers**
=
[Problem Link](https://leetcode.com/problems/count-the-number-of-powerful-integers/description)

## Intuition
To make a problem much easier, we construct a method `count(num)` that counts every powerful integers from 0 to `num`. 
Then we don't have to consider both `start` and `finish` simultaneously, just return `count(finish)` - `count(start-1)`. 
Now the most complex part comes from how to deal with edge cases; 1. the largest digit and 2. the smallest digits
correspond to `s`. First of all, prune the case that `num` is equal or less than `s`.

Next, we check general cases. Suppose the first digit `num[0]` is bigger than `limit`, then every digit except 
suffix `s` can be any integer between 0 and `limit`. Then the count is obvious as 
'number of candidates for each digit' power length of prefix. Elif `limit` is bigger, then we divide the problem in 
2 cases by fixing `num[0]`:

1. `num[0]` < `limit`
    - Similar to the above `num[0]` >= `limit` case.
    - Except `num[0]`, all the other digits can be any integer between 0 and `limit`.

2. `num[0]` == `limit`
    - `num[0]` is fixed, so counting next integers is a new subproblem of `num[1:]`.

With these two approaches and for-loop, we can solve subproblems sequentially.

Finally, we check the last candidate of powerful integer, that is, the maximum powerful integer concluded from the 
above general case + suffix `s`.

## Approach
**Step-by-Step Process**

1. Define a method `count` to count the number of powerful integers between 0 and `nums` as follows.
    - The answer will be `count(finish)` - `count(start-1)`.

2. Check the edge case of `len(num)` <= `len(s)`.

3. In general cases, divide the problem in 3 ways whether `num[0]` is larger or smaller than or equal to `limit`.
    - If `num[0]` is strictly larger, then every digit can be chosen.
    - If `num[0]` is strictly smaller, then every digit except `num[0]` can be randomly chosen.
    - If `num[0]` is equal to `limit`, then by fixing `num[0]` the task is now a subproblem of `num[1:]`.

4. Check the maximum candidate of powerful integer.

## Solutions
```python
# Time Complexity O(len(finish)) ~ O(1), Space Complexity O(1)
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(num: str):
            if len(num) < len(s):
                return 0

            if len(num) == len(s):
                return 1 if num >= s else 0

            cnt = 0
            prefix_len = len(num) - len(s)

            for i in range(prefix_len):
                digit = int(num[i])
                
                if digit > limit:
                    cnt += (limit+1) ** (prefix_len-i)

                    return cnt

                else:
                    cnt += digit * (limit+1) ** (prefix_len-i-1)

            if num[-len(s):] >= s:
                cnt += 1

            return cnt


        return count(str(finish)) - count(str(start-1))
