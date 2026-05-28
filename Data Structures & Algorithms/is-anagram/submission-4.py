class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sChars = defaultdict(int)
        tChars = defaultdict(int)

        for char in s:
            sChars[char] += 1
            
        for char in t:
            tChars[char] += 1

        return sChars == tChars
        