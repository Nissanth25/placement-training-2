class Solution(object):
    def getDecimalValue(self, head):
        c= head
        s=""
        while c:
            s=s+str(c.val)
            c=c.next
        return int(s,2)
