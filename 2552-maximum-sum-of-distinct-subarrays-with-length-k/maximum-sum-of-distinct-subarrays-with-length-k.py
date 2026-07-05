class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        summ=0
        maxx=0
        hashmap={}
        dup=0
        for i in range(k):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=0
            hashmap[nums[i]]+=1
            summ=summ + nums[i]
            if hashmap.get(nums[i],0)>1:
                dup+=1
        if dup==0:
            maxx=max(maxx,summ)

        for j in range(k,len(nums)):
            numstoadd=nums[j]
            numstoremove=nums[j-k]

            if numstoadd not in hashmap:
                hashmap[numstoadd]=0
            hashmap[numstoadd]+=1

            if hashmap[numstoadd]>1:
                dup+=1
            summ=summ+numstoadd

            if hashmap.get(numstoremove,0)>1:
                dup-=1
            
            hashmap[numstoremove] -=1
            summ=summ-numstoremove

            if dup==0:
                maxx=max(summ,maxx)
        return maxx