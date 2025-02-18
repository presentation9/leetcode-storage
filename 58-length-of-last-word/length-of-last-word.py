class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        lastword = words[-1]
        return len(lastword)