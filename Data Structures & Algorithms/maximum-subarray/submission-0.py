class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kind of like sliding window
        #We can do a bit of pruning if its not more than the element
        maxSub = nums[0]
        currSum = 0

        for i in nums:
            if(currSum < 0):
                currSum = 0
            currSum += i
            maxSub = max(maxSub, currSum)
        return maxSub
