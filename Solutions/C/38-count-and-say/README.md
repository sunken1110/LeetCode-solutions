**Count and Say**
=
[Problem Link](https://leetcode.com/problems/count-and-say/description)

## Intuition
We simply use recursion to generate all count-and-say sequences.

## Approach
**Step-by-Step Process**

1. If `n = 1`, return 1.

2. In each level, we loop from the previous string of coun-and-say sequence. 

3. Process RLE, while storing previous character.
    - While visiting same integer, count the number.
    - If we meet any distinct integer, concatenate count and the previous integer, and add to final string `s`.
  
## Solutions
```python
# Time Complexity O(2^n), Space Complexity O(2^n)
class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'

        if n == 1:
            return curr

        for _ in range(2, n+1):
            n_len = len(curr)
            s = ''
            cnt = 1
            char = curr[0]

            for i in range(1, n_len):
                if char != curr[i]:
                    s += str(cnt) + char
                    char = curr[i]
                    cnt = 1

                else:
                    cnt += 1

            s += str(cnt) + char
            curr = s

        return curr
