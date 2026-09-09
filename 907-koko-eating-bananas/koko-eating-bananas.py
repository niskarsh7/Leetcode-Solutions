class Solution:
    def isPossible(self,piles,speed,hours):
        totalhours=0
        for pile in piles:
            totalhours+= math.ceil(pile/speed)
        return totalhours<=hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minn=1
        maxx=float('-inf')
        for pile in piles:
            maxx=max(pile,maxx)
        low=minn
        high=maxx
        while low < high:
            mid = low + (high- low)//2
            if self.isPossible(piles,mid,h):
                high=mid
            else:
                low=mid+1
        return low