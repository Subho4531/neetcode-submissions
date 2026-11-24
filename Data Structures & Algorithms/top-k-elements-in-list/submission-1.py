class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h={}

        for n in nums:
            h[n] = h.get(n, 0) + 1

        return [item[0] for item in sorted(h.items(), key=lambda x: x[1], reverse=True)[:k]]