class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        if x>=0:
            ori=x
            r_n=0

            while x>0:

                
                a=x%10

                r_n=r_n*10+a
                x//=10
            if r_n==ori:
                return True
            return False
        else:
            return False


        