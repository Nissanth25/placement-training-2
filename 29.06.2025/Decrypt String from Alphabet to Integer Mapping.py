class Solution(object):
    def freqAlphabets(self, s):
        for i in range(10,27):
            s = s.replace( str(i) + '#',chr(ord('j') - 10 + i) )
        for i in range(1,10):
            s = s.replace( str(i), chr(ord('a') - 1 + i ) )
        return s
