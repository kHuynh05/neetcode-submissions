class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        p = {}
        for i in nums:
            if i in p:
                return True
            else:
                p[i] = 1
        return False
