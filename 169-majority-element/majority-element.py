class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset={}
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset[nums[i]]=1
            else:
                hashset[nums[i]]+=1
        return max(hashset,key=hashset.get)    