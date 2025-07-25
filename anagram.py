class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        inp = list(s.lower())
        out = list(t.lower())
        inp.sort()
        out.sort()
        return inp==out

        