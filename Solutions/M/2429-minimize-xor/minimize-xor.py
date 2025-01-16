#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/minimize-xor/description

# Complexity O(max(len(bin(num1)), len(bin(num2))))
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        max_bit = max(len(bin(num1)), len(bin(num2))) - 2    # remove a type info '0b'

        bit_num1 = bin(num1)[2:].rjust(max_bit, '0')
        bit_num2 = bin(num2)[2:]

        set_bit = sum(int(x) for x in bit_num2)
        ans = ['0'] * max_bit

        for i in range(len(bit_num1)):
            if bit_num1[i] == '1':
                ans[i] = '1'
                set_bit -= 1

                if set_bit == 0:
                    break

        if set_bit != 0:
            for j in range(len(bit_num1) - 1, -1, -1):
                if bit_num1[j] == '0':
                    ans[j] = '1'
                    set_bit -= 1

                    if set_bit == 0:
                        break

        return int(''.join(ans), 2)
