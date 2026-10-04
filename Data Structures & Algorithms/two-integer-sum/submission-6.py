class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {}
        
        for i in range(len(nums)):
            condition = target - nums[i]
            if(condition in prevNum):
                return [prevNum[condition], i]
            prevNum[nums[i]] = i
                
        