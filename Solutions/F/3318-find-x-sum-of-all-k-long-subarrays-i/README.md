**Find X-Sum of All K-Long Subarrays I**
=
[Problem Link](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description)

## Intuition
We use sliding window technique to search each `n-k+1` width window. Start from the leftmost window `nums[:k]`, 
count the frequency of each integer with `Counter`. To find top `x` most frequent elements, we sort it by the 
frequency and append the `x`-sum to the answer array. Then move to the next window; decrease a frequency of 
the first element and increase a frequency of `k+1`th element manually. Repeat the process until the final 
window is checked.

## Approach
**Step-by-Step Process**

1. Initialize `ans` and count the frequency `freq` of first window.

2. Sort `freq` to extract top `x` most frequent elements.
    - Store top `x` elements to `top_x`.
    - For `num` in `top_x`, compute the `x`-sum and append to `ans`.

3. Move to the next window and update `freq`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        freq = Counter(nums[:k])

        for i in range(n-k+1):
            sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
            top_x = set(num for num, _ in sorted_freq[:x])
            x_sum = 0

            for num in top_x:
                x_sum += num * freq[num]

            ans.append(x_sum)

            if i + k < n:
                freq[nums[i]] -= 1
                freq[nums[i+k]] += 1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]

        return ans
```
