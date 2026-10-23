class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            print(a)
            if(a > 0):
                break
            elif(i > 0 and nums[i-1] == a):
                continue
            print("check")
            left, right = i+1, len(nums)-1

            while(left < right):
                if(a + nums[left] + nums[right] > 0):
                    right -= 1
                elif(a + nums[left] + nums[right] < 0):
                    left += 1
                else:
                    res.append([a,nums[left],nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res