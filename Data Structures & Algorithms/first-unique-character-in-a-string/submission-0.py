class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for i, ch in enumerate(s):
            if count[ch]==1:
                return i
        return -1