class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if(nums[i] in diff):
                return [diff[nums[i]], i]
            diff[sub] = i
            
            