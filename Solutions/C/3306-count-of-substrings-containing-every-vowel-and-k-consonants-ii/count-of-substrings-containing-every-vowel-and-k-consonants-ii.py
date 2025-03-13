#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description

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
