class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for word in strs:
            tmp = "".join(sorted(word))
            if tmp in final:
                final[tmp].append(word)
            else:
                final[tmp] = [word]
        
        return list(final.values())