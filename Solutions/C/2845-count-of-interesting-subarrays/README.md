**Count of Interesting Subarrays**
=
[Problem Link](https://leetcode.com/problems/count-of-interesting-subarrays/description)

## Intuition
To check how many subarrays are interesting, we first fix the rightmost index of main array. 
Suppose this array has `x` elements that modulo is `k`. An interesting subarray must have `k` such element modulo 
`modulo`, we need to pop `x-k (mod k)` of them from left to right. To efficientyl compute, we use prefix sum here. 
While scanning `nums` from left to right, count prefix sum `pref` that is `k` modulo `modulo`. Since the gap is 
`(prefix - k)`, check the number of pre-calculated prefix sum of `(prefix - k)` and add it to the total count. 

## Approach
**Step-by-Step Process**

1. Initialize prefix count `freq` that stores the count of each modulos.
    - `freq[0] = 1` since an empty array is modulos 0.
  
2. Each step of scanning `num` in `nums`, check the modulo and add to `prefix`.

3. Calculate `gap` needed to be removed from the left elements, to be an interesting subarray.

4. Count a number of such proper elements by using pre-computed `freq`.

5. Adjust the modulo of `num` to `freq`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        cnt = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1

            curr = prefix % modulo
            gap = (modulo + curr - k) % modulo
            cnt += freq[gap]
            freq[curr] += 1

        return cnt
