class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for word in strs:
            tmp = "".join(sorted(word))
            if tmp in final:
                final[tmp].append(word)
            else:
                final[tmp] = [word]
        
        final_out = []
        for s in final:
            word_comp = []
            for w in final[s]:
                word_comp.append(w)
            final_out.append(word_comp)
        return final_out