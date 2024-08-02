class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split() #convert string to list, splitting at whitespaces
        return len(s[-1]) #return length of last word in list
