**Count the Number of Good Subarrays**
=
[Problem Link](https://leetcode.com/problems/count-the-number-of-good-subarrays/description)

## Intuition
Since a subarray is a contiguous sequence, we can apply sliding window technique. For convenient, let good pair be `(i, j)` 
such that `i < j` and `nums[i] == nums[j]`. We track the frequency of each values of `nums` and count `cnt` of good pairs. 
Note that `cnt` is cumulative, and if a subsequence is good then any super subsequence of it is also good.

## Approach
**Step-by-Step Process**

1. For an easy use, set the frequency of each value `freq` as `defaultdict`

2. Expand the right window `right` and adjust `freq` of new value.
    - `cnt` may increase if this value is already seen, which value is exactly `freq[nums[right]]`.

3. If a contiguous subsequence is good, then add the count of good subsequences of fixed left window.

4. Shrink the left window `left` until the subsequence is no more good.
    - During this sequence, keep adding the count of good subsequence.
    - And then decrease `freq` and `cnt`, and increase `left`.

5. Repeat expanding right window and shrink left window until the end.
  
## Solutions
```python
# Complexity O((right-left) * sqrt(right))
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num == 1:
                return False

            for div in range(2, int(sqrt(num)) + 1):
                if num % div == 0:
                    return False

            return True
        
        ans = []
        prev = None

        for num in range(left, right + 1):
            if not is_prime(num):
                continue

            if not prev:
                prev = num
                continue

            diff = num - prev

            if diff <= 2:
                return [prev, num]

            if not ans or diff < ans[1] - ans[0]:
                ans = [prev, num]

            prev = num

        return [-1, -1] if not ans else ans
