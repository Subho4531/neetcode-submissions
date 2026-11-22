class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store=[]

        if len(strs)==1:
            return [strs]

        hashmap = {}

        for index,word in enumerate(strs):
            key = tuple(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]

        return list(hashmap.values())