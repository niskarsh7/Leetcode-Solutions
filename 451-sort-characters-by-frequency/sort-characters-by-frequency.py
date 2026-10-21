class Solution:
    def frequencySort(self, s: str) -> str:
        lst=list(s)
        hashtable=Counter(lst)
        sorted_hash=sorted(hashtable.items() , key=lambda items :items[1],reverse=True)
        sorted_dic=dict(sorted_hash)
        build=[key for key,value in sorted_dic.items() for _ in range(value)]
        return "".join(build)