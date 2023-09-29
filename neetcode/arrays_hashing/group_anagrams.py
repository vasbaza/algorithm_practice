from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return res.values()
    
    def groupAnagramsNotOptimal(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for i, str in enumerate(strs):
            sortedStrArray = sorted(str)
            sortedStr = "".join(sortedStrArray)
            if d.get(sortedStr, 0) != 0:
                d[sortedStr].append(str)
            else:
                d[sortedStr] = [str]

        return list(d.values())

    def isValidAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[s[i]] = countT.get(t[i], 0) + 1
        
        for key in countS:
            if countS[key] != countT[key]:
                return False
            
        return True
    