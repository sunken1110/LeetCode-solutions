**Total Characters in String After Transformations II**
=
[Problem Link](https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/description)

## Intuition
This problem is more tricky version of the following problem:
[Problem Link](https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description)

The main idea is to convert the transformation as a linear transformation in the sense of linear algebra. 
If `T` is such a linear map, then the problem is to calculate `T^t (freq)` where `freq` is the counter matrix of `s`. 
We define `matmul` of matrix multiplication method and `matexp` of matrix exponentation method. For the efficiency of 
`matexp`, we use a bit operation. For an example, suppose `t = 27`. In binary, `t = 11011` and `T^t` can be computed like

- T^27 = T * (T^2)^13 = T * T^2 * (T^4)^6 = T * T^2 * (T^8)^3 = T * T^2 * T^8 * T^16

In this factorization we only need 4 (`O(log(n))`) `matexp`, not 27 (`O(n)`). 


## Approach
**Step-by-Step Process**

1. Initialize `freq` of counter matrix of `s`.

2. Construct a linear transformation `mul`.

3. Define matrix multiplication method `matmul`.

4. Define matrix exponentation method `matexp` based on `matmul`.
    - For the time efficiency, we use a binary factorization approach.
  
5. Compute `matmul([freq], matexp(mul, t))` modulo (10**9 + 7).
  
## Solutions
```python
# Time Complexity O(s + n^3 * t), Space Complexity O(n^2)
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        freq = [0] * 26
        mul = [[0] * 26 for _ in range(26)]
        mod = 10**9 + 7
        
        for char in s:
            freq[ord(char) - ord('a')] += 1

        for i in range(26):
            for num in range(nums[i]):
                mul[i][(i+1+num) % 26] += 1

        
        def matmul(A, B):
            rowA = len(A)
            colA = len(A[0])
            colB = len(B[0])
            mat = [[0] * colB for _ in range(rowA)]

            for i in range(rowA):
                for j in range(colB):
                    tmp = 0
                    for k in range(colA):
                        tmp += A[i][k] * B[k][j] % mod

                    mat[i][j] = tmp

            return mat


        def matexp(A, exp):
            n = len(A)
            mat = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

            while exp > 0:
                if exp & 1:
                    mat = matmul(mat, A)

                A = matmul(A, A)
                exp >>= 1

            return mat


        ans = 0
        freq = matmul([freq], matexp(mul, t))

        return sum(freq[0]) % mod
```
