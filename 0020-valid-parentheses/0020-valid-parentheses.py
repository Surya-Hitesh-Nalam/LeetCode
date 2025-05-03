class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l=[]
        for i in s:
            if len(l)>0 and ((i==')' and l[-1]=='(') or (i=='}' and l[-1]=='{') or(i==']' and l[-1]=='[')):
                l.pop()
            else:
                l.append(i)
        return len(l)==0
        