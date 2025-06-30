class Solution(object):
    def reorderSpaces(self, text):
        l, s, w, word, words = len(text), 0, 0, '', []
        c_pre = None
        for i,c in enumerate(text):
            if c==' ':
                s += 1 
            else:
                word += c 
                
            if (i==0 and c!=' ') or (c_pre==' ' and c!=' '):
                w += 1
            if (c==' ' and c_pre!=' ') or (i==l-1 and c!=' '): 
                if word: words.append(word)
                word = ''
            c_pre = c      
        if w>1:
            n, r = s//(w-1), s%(w-1) 
            res = ''
            for word in words[:-1]:
                res = res + word + ' '*n
            return res + words[-1] + ' '*r
        else:
            return words[0] + ' '*s
