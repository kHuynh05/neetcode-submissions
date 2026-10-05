class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #make set and check for longest
        x = set(nums)
        longest = 0

        for i in x:
            #check for shorter value and if shorter move on and start from there
            if(i-1 not in x):
                length = 1
                while(i+length in x):
                    length+=1
                longest = max(longest,length)
        return longest