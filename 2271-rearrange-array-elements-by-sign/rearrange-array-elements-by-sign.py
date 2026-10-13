class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=[x for x in nums if x>0]
        neg=[x for x in nums if x<0]
        res=[]
        p1=0
        p2=0
        for i in range(len(nums)):
            if i%2==0:
                res.append(pos[p1])
                p1+=1
            else:
                res.append(neg[p2])
                p2+=1
        return res
