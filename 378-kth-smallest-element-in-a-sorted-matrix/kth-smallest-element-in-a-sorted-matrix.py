class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        min_heap=[]
        for i in range(len(matrix)):
            heapq.heappush(min_heap,(matrix[i][0],i,0))
        counter=1
        while min_heap:
            val,list_id,ele_id=heapq.heappop(min_heap)
            if counter==k:
                return val
            counter+=1
            nextele_id=ele_id+1
            if (nextele_id)<len(matrix):
                heapq.heappush(min_heap,(matrix[list_id][nextele_id],list_id,nextele_id))
        return -1  