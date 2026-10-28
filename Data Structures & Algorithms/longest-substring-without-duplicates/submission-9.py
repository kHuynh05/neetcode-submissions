class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #instantiate var to hold character and index + output and left pointer
        mp = {}
        l = 0
        output = 0

        #for loop to go through each character, use r as a right pointer
        for r in range(len(s)):
            #if the value is already in the character, move the left pointer
            if(s[r] in mp):
                l = max(mp[s[r]] + 1,l)
            #add to dict
            mp[s[r]] = r
            output = max(r - l + 1,output)

        return output