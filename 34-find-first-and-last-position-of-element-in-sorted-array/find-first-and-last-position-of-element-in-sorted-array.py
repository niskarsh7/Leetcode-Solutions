class Solution:
    def firstoccurence(self, nums , target):
        low=0
        high=len(nums)-1
        ans=-1
        while low<=high:
            mid = low+(high-low)//2

            if nums[mid]== target:
                ans=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans

    def lastoccurence(self, nums , target):
        low=0
        high=len(nums)-1
        ans=-1
        while low<=high:
            mid = low+(high-low)//2

            if nums[mid]==target:
                ans=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        firstIndx=self.firstoccurence(nums,target)
        lastIndx=self.lastoccurence(nums,target)
        
        if firstIndx==-1:
            return[-1,-1]
        else:
            return[firstIndx,lastIndx]