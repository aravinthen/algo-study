class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]

        i1 = 0
        i2 = len(s)-1

        if len(s) == 1:
            return True

        while i1 < i2:
            if s[i1] != s[i2]:
                return False
            
            i1+=1
            i2-=1
        
        return True