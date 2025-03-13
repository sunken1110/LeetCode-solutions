**Count of Substrings Containing Every Vowel and K Consonants II**
=
[Problem Link](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description)

## Intuition
The point is to find a proper window, i.e., a substring that holds the condition. Suppose we extend 
the right side of window. 
Since there is a constraint that the number of consonants must be equal to `k`, 
if the window meets `k+1`th consonant then the left side of the leftmost consonant must be discarded. 
To iterating the process, we check two pointers of a window, namely `left` and `right`. 
We check vowel condition with `defaultdict(int)` with `len(vowel_cnt) == 5`. With discarding process, 
we need extra method that removes the leftmost character of window from `vowel_cnt`.

## Approach
**Step-by-Step Process**

1. Initialize the conditions `vowel_cnt = defaultdict(int)` and `conso_cnt = 0`.

2. Define a method `remove_left` that discards a character from `vowel_cnt`.

3. Extend a window from left side until the conditions hold.

4. Eventually, this window meet `k+1`th consonant. Then shrink it from the left until meet 1st consonant.
    - While shrinking, count every possible substrings `cnt`.
    - This process yields every possible substring of the window with `right` right frame.
  
5. Now reset `cnt`. Search `k+2`th consonant, shrink left frame, then count. Repeat until finish.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowel_cnt = defaultdict(int)
        conso_cnt = 0
        vowel = 'aeiou'
        cnt = 0
        ans = 0


        def remove_left(char):
            if char in vowel:
                vowel_cnt[char] -= 1
                if vowel_cnt[char] == 0:
                    del vowel_cnt[char]

            else:
                nonlocal conso_cnt
                conso_cnt -= 1

        
        left = 0
        for right in range(n):
            if word[right] in vowel:
                vowel_cnt[word[right]] += 1

            else:
                conso_cnt += 1
                cnt = 0

            while conso_cnt > k:
                remove_left(word[left])
                left += 1

            while conso_cnt == k and len(vowel_cnt) == 5:
                cnt += 1
                remove_left(word[left])
                left += 1

            ans += cnt

        return ans
