**Count the Number of Arrays with K Matching Adjacent Elements**
=
[Problem Link](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description)

## Intuition
2 main ideas are used: 
- To consider two adjacent elements as one element.
- Construct an matching map first and then allocate the integers.

 Suppose `n=5` and `k=2` case with non-allocated length 5 array     
### O-O-O-O-O
Let `=` denotes the matching relation, and consider a matching map
 
### O=O-O=O-O
Since matching two adjacent elements are equal, this is exactly same with 

### (O=O)-(O=O)-O <-> O-O-O
That is, we only have to allocate 3(=`n-k`) integers and no two adjacent elements are equal.

The task is to compute the number of possible matching maps and possible allocations, and then multiply them. 

## Approach
**Step-by-Step Process**

1. We need `k` matching (`=`) from `n-1` potential matching relation (`-`), so `n-1` choose `k` matching maps exist.

2. We need `n-k` elements with no adjacent matching. Choose freely `m` element for the first element, then all the remained elements have `m-1` possible cases. Thus, we have `m * (m-1)^(n-k-1)`.

3. To avoid abundant computation, pre-compute `n` choose `k` for given constraints.
> For the computing efficiency, we define `nCk` rather than `math.comb`. Since our mod=10**9+7 is a prime and x^(mod-1) = 1 (modulo mod) by the Euler's modulo arithmetic, `pow(x, mod-2, mod)` is equivalent to the dvision by `x`. Then `nCk = n! / k!(n-k)!` is equivalent to `n! * pow(k, mod-2, mod) * pow(n-k, mod-2, mod)`. 
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
upper = 10**5 + 1
mod = 10**9 + 7
nom = [1] * upper
denom = [1] * upper

for i in range(1, upper):
    nom[i] = i * nom[i-1] % mod
    denom[i] = pow(nom[i], mod-2, mod)


def nCk(n, k):
    return nom[n] * denom[k] * denom[n-k] % mod


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return nCk(n-1, k) * m * pow(m-1, n-k-1, mod) % mod
