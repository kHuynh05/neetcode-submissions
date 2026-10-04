class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search with left,mid, and right
        minE = nums[0]
        l,r = 0, len(nums)-1

        while(l <= r):
            #if left element is less than right element, res = nums[l] potentially
            if(nums[l] < nums[r]):
                minE = min(minE, nums[l])
                break
            
            #binary search here
            mid = ((l + r) // 2)
            minE = min(nums[mid],minE)
            if(nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid - 1

        return minE