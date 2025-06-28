class Solution(object):
    def sortString(self, s):
        l=[0]*26
        for ch in s:
            l[ord(ch)-97]+=1
        ans=''
        while sum(l)!=0:
            for i in range(0,26):
                if l[i]:
                    ans+=chr(i+97)
                    l[i]-=1
            for i in range(25,-1,-1):
                if l[i]:
                    ans+=chr(i+97)
                    l[i]-=1
        return ans
