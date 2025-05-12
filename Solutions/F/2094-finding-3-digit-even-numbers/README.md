**Finding 3-Digit Even Numbers**
=
[Problem Link](https://leetcode.com/problems/finding-3-digit-even-numbers/description)

## Intuition
We first count the frequency of each digit in `digits`. Since we have to check every possiblility of 3-digit numbers, 
backtracking is a good approach. While scanning the candidate of each degree, exclude the case of leading zero and odd 
number in the last digit. To avoid `sort`, we check integers from 0 to 9 in ascending order for each digit.

## Approach
**Step-by-Step Process**

1. Count the number of each digit with `freq = defaultdict(list)`.

2. Construct a backtracking algorithm on the digit `i`, with the following assertions:
    - `i` is in `freq` with positive counts.
    -  no leading zero.
    -  even `i` for the 3rd digit.
  
## Solutions
```python
# Time Complexity O(1), Space Complexity O(1)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = defaultdict(int)
        ans = []
        for i in digits:
            freq[i] += 1


        def backtrack(num, idx):
            if idx == 3:
                ans.append(num)

                return

            for i in range(10):
                if not freq[i] or (idx == 0 and i == 0) or (idx == 2 and i % 2):
                    continue

                freq[i] -= 1
                backtrack(num*10+i, idx+1)
                freq[i] += 1

        
        backtrack(0, 0)

        return ans
```
