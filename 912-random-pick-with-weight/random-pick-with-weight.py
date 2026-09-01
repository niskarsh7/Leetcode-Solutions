class Solution:

    def __init__(self, w: List[int]):
        self.psums=[0]*len(w)
        self.psums[0]=w[0]

        for i in range(1,len(w)):
            self.psums[i]=self.psums[i-1]+w[i]
        

    def pickIndex(self) -> int:
        low=0
        high=len(self.psums)-1
        rand=random.random()
        target=rand*self.psums[-1]
        while (low < high):
            mid = low + (high-low)//2

            if (target<=self.psums[mid]):
                high=mid
            else:
                low=mid+1
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()