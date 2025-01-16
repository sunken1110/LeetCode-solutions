**Minimize XOR**
=
[Problem Link](https://leetcode.com/problems/minimize-xor/description)

## Intuition
The task is to minimize `num1` by `XOR`. To acquire the minimum, we simply flip `1`s to `0`s as many as possible 
which starts from the most significant bit (with a binary expression of `num1`, from the leftmost `1` to the right).
Since this process continues until the number of set bits of `num2` has been excuted, if no more `1` exists in `num1` then
we now flip `0`s to `1`s starts from the least significant bit (from the rightmost `0` to the left).

## Approach
**Step-by-Step Process**

1. Calculate the maximum bit length `max_bit` of `num1` and `num2` in binary expression.

2. Adjust `num1` to the length of `max_bit`, to clarify exchangable bits.

3. Calculate set bits `set_bit` of `num2`, to track the total number of required processes.

4. Flip `1`s to `0`s in `num1` starting from the most significant bit.
    - If the process executed `set_bit` times during the right-side traverse, break.
    - Count the remained number of execution by `set_bit`.
  
5. If any execution is still remained after the above iterations, now traverse reversely to flip `0`s to `1`s in `num1`.
    - If the process executed remained `set_bit` times during the left-side traverse, break.
   
## Solutions
```python
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
```
