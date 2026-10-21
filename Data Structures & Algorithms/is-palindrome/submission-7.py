class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1;
        
        #while left does not meet right
        while(left <= right):
            if(not (s[left].isalpha() or s[left].isnumeric())):
                left+=1
            elif(not (s[right].isalpha() or s[right].isnumeric())):
                right -=1
            else:
                if(s[left].lower() != s[right].lower()):
                    return False;
                left+=1
                right-=1
        return True