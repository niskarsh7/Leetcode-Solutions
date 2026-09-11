class Solution:
    def isPossible(self,val, index,n,maxSum):
        totalsum=0
        if (val<=index):
            totalsum=totalsum+(val*(val+1)//2)+(index-val+1)
        else:
            totalsum=totalsum + (val+val-index)*(index+1)//2
        
        if (val>=n-index):
            totalsum=totalsum+(2*val+index-n+1)*(n-index)//2
        else:
            totalsum=totalsum+(val*(val+1)//2)+(n-index-val)
        return totalsum-val<=maxSum
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low=1
        high=maxSum
        while low < high:
            mid=low+(high-low)//2
            if not self.isPossible(mid,index,n,maxSum):
                high=mid
            else:
                low=mid+1

        return low if self.isPossible(low,index,n,maxSum) else low-1     