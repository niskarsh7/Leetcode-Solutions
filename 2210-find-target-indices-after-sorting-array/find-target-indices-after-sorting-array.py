class Solution:
    def first(self,nums,target):
        low=0
        high=len(nums)-1
        ans1=-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid]==target:
                ans1=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans1
    def last(self,nums,target):
        low=0
        high=len(nums)-1
        ans2=-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid]==target:
                ans2=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans2
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        f=self.first(nums,target)
        l=self.last(nums,target)
        if f==-1:
            return []
        return list(range(f,l+1))