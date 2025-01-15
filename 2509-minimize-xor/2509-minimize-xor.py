class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bitCount = bin(num2).count('1') 
        bitCount -= bin(num1).count('1')  
        cur = 1
        while bitCount != 0:
            if bitCount < 0 and (num1 & cur) != 0: 
                num1 ^= cur
                bitCount += 1
            elif bitCount > 0 and (num1 & cur) == 0:  
                num1 |= cur
                bitCount -= 1
            cur <<= 1  
        return num1
        