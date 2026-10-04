class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dynamic programming
        #we need to record both max and min because of negative numbers
        maxP, minP = 1, 1
        res = max(nums)

        for i in nums:
            if i == 0:
                maxP, minP = 1,1
                continue
            
            temp = maxP * i

            maxP = max(maxP*i,minP*i,i)
            minP = min(temp, minP*i,i)
            res = max(res,maxP)

        return res