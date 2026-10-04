class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for i in range(len(nums)):
            if(nums[i] in nums[i+1:len(nums)]):
                return True
         return False