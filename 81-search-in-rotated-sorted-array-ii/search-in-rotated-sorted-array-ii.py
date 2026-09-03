class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low= 0
        high= len(nums)-1

        while (low <=high):
            mid = low + (high-low)//2

            if nums[mid]==target:
                return True
            #Edge condition that prevent from break code
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low=low+1
                high=high-1
            elif nums[low]<=nums[mid]:
            #left part is sorted
                if target>=nums[low] and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
            #right part is sorted
                if target>=nums[mid] and target <=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False