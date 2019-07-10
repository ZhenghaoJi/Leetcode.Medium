class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        l = 0
        r  = len(s) -1
# I don`t know isalnum(), and i used a stupid way to describe number and abc.
# Then I can`t pass 0p  hhh --
        while(l < r):
            if(not s[l].isalnum()):
                l+=1
                continue
            
            if(not s[r].isalnum()):
                r-=1
                continue
            
            if(s[l].lower()!=s[r].lower()):
                return False
            else:
                l+=1
                r-=1
        
        return True
