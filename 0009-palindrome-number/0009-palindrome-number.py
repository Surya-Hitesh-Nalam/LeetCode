class Solution(object):
    def isPalindrome(self, x):
        y=x
        sum=0
        while y>0:
            rem=y%10
            sum=sum*10+rem
            y=y//10
        if x==sum:
            return True
        else:
            return False
        