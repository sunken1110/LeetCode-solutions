**Max Sum of a Pair With Equal Sum of Digits**
=
[Problem Link](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description)

## Intuition
First, define a function `digitSum` to calculate the sum of digits, then we can gather pairs with 
equal sum of digits. Idea is, if we sort `nums` in descending order then at most 2 numbers in each digit sum 
are candidates of max sum.

## Approach
**Step-by-Step Process**

1. Sort `nums` in descending order.

2. Define `digitSum` which calculates the sum of digits.

3. With `sum_set = defaultdict(list)`, push numbers in each digit sum.
    - Since we already ordered `nums`, push occurs at most 2 times per each digit sum.
  
4. Get every keys in `sum_set` which contains exactly 2 values, then find the maximum value of it.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_set = defaultdict(list)
        max_sum = -1

        nums.sort(reverse=True)

        def digitSum(x):
            s = 0

            while x > 0:
                s += x % 10
                x = x // 10

            return s

        for num in nums:
            digit_sum = digitSum(num)

            if len(sum_set[digit_sum]) <= 1:
                sum_set[digit_sum].append(num)

        for num_list in sum_set.values():
            if len(num_list) == 2:
                max_sum = max(max_sum, sum(num_list))

        return max_sum
