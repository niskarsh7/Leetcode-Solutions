class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        maxx=0
        i,j=0,0
        while j < len(fruits):
            fruit=fruits[j]
            count[fruit]=count.get(fruit,0)+1
            while len(count)> 2:
                left_fruit=fruits[i]
                count[left_fruit]-=1
                if count[left_fruit]==0:
                    del count[left_fruit]
                i+=1
            maxx=max(maxx,j-i+1)
            j+=1
        return maxx