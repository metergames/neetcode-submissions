class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for word in strs:
            count = [0] * 26
            for l in word:
                count[ord(l) - ord("a")] += 1
            count_t = tuple(count)
            if count_t in final:
                final[count_t].append(word)
            else:
                final[count_t] = [word]
        
        return list(final.values())