class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        comp = dict()
        for n in nums:
            if n in comp:
                comp[n] += 1
            else:
                comp[n] = 1
        final = []
        for i in range(k):
            ci = max(comp, key=comp.get)
            comp[ci] = 0
            final.append(ci)
        return final