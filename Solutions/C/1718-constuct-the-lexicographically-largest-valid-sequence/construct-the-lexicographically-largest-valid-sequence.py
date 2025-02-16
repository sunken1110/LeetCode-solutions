#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description

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
