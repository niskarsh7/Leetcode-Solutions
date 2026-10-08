class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        min_heap=[]
        visited=set()
        heapq.heappush(min_heap,(nums1[0]+nums2[0],0,0))
        res=[]
        counter=1
        while counter<=k :
            ele=heapq.heappop(min_heap)
            summ= ele[0]
            i=ele[1]
            j=ele[2]
            res.append([nums1[i],nums2[j]])
            if (i+1< len(nums1)):
                pair=(i+1,j)
                if pair not in visited:
                    heapq.heappush(min_heap,(nums1[i+1]+nums2[j],i+1,j))
                    visited.add(pair)
            if (j+1< len(nums2)):
                pair=(i,j+1)
                if pair not in visited:
                    heapq.heappush(min_heap,(nums1[i]+nums2[j+1],i,j+1))
                    visited.add(pair)
            counter+=1
        return res