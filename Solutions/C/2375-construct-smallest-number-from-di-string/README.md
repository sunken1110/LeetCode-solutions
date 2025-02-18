**Construct Smallest Number From DI String**
=
[Problem Link](https://leetcode.com/problems/construct-smallest-number-from-di-string/description)

## Intuition
We suggest 2 approaches; stack and backtracking. 
Since a backtracking is typical, we only explain about stack approach. 
Key idea is that when we meet 'D', a sequence is written reversely until we meet 'I'.
That is, in each step, we stack an integer. If we meet 'I', poping all stacks out. If we meet 'D', 
then just stack an integer until we meet 'I'. 
Stack's LIFO structure guarantees a reversed sequence.

## Approach
**Step-by-Step Process**

1. Starts by initialize `stack = ['1']`, and a required sequence `seq`.

2. For each character of pattern, we stack an integer to `stack`.

3. If we meet 'D', then just stack. If we meet 'I', then poping all stack out and add to `seq`.

4. After iteration, pop and add a remaining stack to `seq`.
    - This is an insurance step for the case of `pattern` finished by 'D'.
  
## Solutions
```python
# Complexity O(n)
class Solution1:
    def smallestNumber(self, pattern: str) -> str:
        stack = ['1']
        seq = ''

        for i in range(len(pattern)):
            if pattern[i] == 'I':
                while stack:
                    seq += stack.pop()

            stack.append(str(i+2))

        while stack:
            seq += stack.pop()

        return seq


# Complexity O(2^n * n) - Backtracking
class Solution2:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        check = set()
        seq = []

        def backtrack(idx):
            if len(seq) == n + 1:
                return seq

            for i in range(1, 10):
                if i in check:
                    continue

                if idx == 0 or (pattern[idx-1] == 'I' and seq[-1] < i) or \
                    (pattern[idx-1] == 'D' and seq[-1] > i):
                    check.add(i)
                    seq.append(i)

                    backtrack(idx + 1)

                    if len(seq) == n + 1:
                        return seq

                    seq.pop()
                    check.remove(i)

        return ''.join(map(str, backtrack(0)))
```
