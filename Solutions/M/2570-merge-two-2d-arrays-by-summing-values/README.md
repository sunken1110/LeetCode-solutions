**Merge Two 2D Arrays by Summing Values**
=
[Problem Link](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description)

## Intuition
Trace the `id`s of arrays in ascending order. Compare the `val`s, then merge two arrays. 
According to the result of comparison, raise the index of `id`s.

## Approach
**Step-by-Step Process**

1. Initialize the current indicies of `nums1` and `nums2`, namely `i` and `j`, respectively.

2. Compare the `val`s of current indices.
    - If same, then raise both `i` and `j`.
    - If the `id` of `nums1` is smaller, then raise `i` only.
    - If the `id` of `nums2` is smaller, then raise `j` only.

3. If either `i` or `j` reach to the boundary, merge the remained part of the other array.

## Solutions
```python
# Complexity O(n)
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []

        i, j = 0, 0
        while i < n1 or j < n2:
            id1 = 1200 if i == n1 else nums1[i][0]
            id2 = 1200 if j == n2 else nums2[j][0]

            if id1 == id2:
                ans.append([id1, nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

            elif id1 < id2:
                ans.append(nums1[i])
                i += 1

            else:
                ans.append(nums2[j])
                j += 1

        return ans
```
