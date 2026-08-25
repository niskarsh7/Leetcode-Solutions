import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        s=str(num)
        even,odd=[],[]
        for item in s:
            val=int(item)
            if val%2==0:
                heapq.heappush(even,-val)
            else:
                heapq.heappush(odd,-val)
        arr=[]
        for item in s:
            val =int(item)
            if val%2==0:
                arr.append(str(-heapq.heappop(even)))
            else:
                arr.append(str(-heapq.heappop(odd)))
        return int("".join(arr))