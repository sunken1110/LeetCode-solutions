**Finding Pairs With a Certain Sum**
=
[Problem Link](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description)

## Intuition
Use `Counter` to count the number of specific target value. When `self.add` is called, adjust `self.freq2`, the
counter of `nums2`, and use `get` method of dictionary in `self.count`.

## Approach
**Step-by-Step Process**

1. Use `Counter` to count the frequency of `nums2`.

2. Implement `self.add` and adjust `self.freq2`.

3. Implement `self.count` by using `get` method.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)        

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        curr = prev + val
        self.nums2[index] = curr
        self.freq2[prev] -= 1
        self.freq2[curr] += 1        

    def count(self, tot: int) -> int:
        cnt = 0

        for num1 in self.nums1:
            cnt += self.freq2.get(tot - num1, 0)

        return cnt


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```
