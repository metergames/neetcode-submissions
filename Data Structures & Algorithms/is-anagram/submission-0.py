class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        for l in s:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
        
        for l2 in t:
            if l2 in letters:
                letters[l2] -= 1
            else:
                return False
        
        for l3 in letters:
            if letters[l3] != 0:
                return False

        return True