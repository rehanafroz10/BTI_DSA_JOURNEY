class Solution:
    def reverse(self, x: int) -> int:
        res, sign = 0, 1

        if x <0:
            sign=-1
            x=-1*x
        
        while x>0:
            res = res * 10 + x % 10
            x //= 10
            
        res *= sign
        
        return res if -2**31 <= res <= 2**31 - 1 else 0
        