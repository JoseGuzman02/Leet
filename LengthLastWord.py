class Solution(object):
    def lengthOfLastWord(self, s):
        temp = s.strip().split(" ")
        length = len(temp)
        return len(temp[length - 1])
