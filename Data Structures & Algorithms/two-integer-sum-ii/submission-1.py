class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if(numbers[l] + numbers[r] == target):
                return [l+1,r+1]

            total = numbers[l] + numbers[r]
            if(total > target):
                r -=1
            else:
                l +=1
        
        return