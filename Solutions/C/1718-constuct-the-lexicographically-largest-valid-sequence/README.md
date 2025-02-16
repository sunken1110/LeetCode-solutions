**Construct the Lexicographically Largest Valid Sequence**
=
[Problem Link](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description)

## Intuition
We use backtracking while fill the sequence from left to right indices. 
To get the lexicographically largest sequence `seq`, we push integers in descending order. 
Once an integer `i` is inserted to `seq`, the position of corresponding second `i` is automatically decided. 
If that position is already filled by the other integer, we adjust the original position of `i`.

## Approach
**Step-by-Step Process**

1. Initialize the largest valid sequence as `seq`.
    - Since there are one 1 and two other integers in `seq`, the length `len_seq` is `2*n - 1`.
  
2. To track already filled integers, we define `used = set()`.

3. Declare backtracking algorithm which takes `idx`, the index of `seq`, as argument.
    - Finishing condition is if a sequence is completed, i.e., `idx == len_seq`.
    - If the position `idx` is already filled by other integer, we move to next index `idx + 1`.
    - To fulfill the lexicographically largest condition, we insert numbers in descending order.
    - If `idx` and corresponding `num` is fixed, we also fill `idx + num` as `num`.
    - Move to the next backtracking of `idx + 1`.
      > If backtracking terminated before fully constructed, reset `idx` and `idx + num` and backtrack with `num - 1`.
  
## Solutions
```python
# Complexity O(n^n)
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_seq = 2*n - 1
        seq = [0] * len_seq
        used = set()

        def backtrack(idx):
            # Sequence completed
            if idx == len_seq:
                return True

            # Already filled by other integer 
            if seq[idx]:
                return backtrack(idx + 1)

            for num in range(n, 0, -1):
                if num in used:
                    continue

                next_idx = idx + num if num > 1 else idx

                if next_idx >= len_seq or seq[next_idx] != 0:
                    continue

                seq[idx] = seq[next_idx] = num
                used.add(num)

                if backtrack(idx + 1):
                    return True

                seq[idx] = seq[next_idx] = 0
                used.remove(num)

            return False

        backtrack(0)

        return seq
```
