class Solution:
    def solver(self,A):
        for i in range(0,len(A),2):
            a,b = A[i], A[i+1]
            for _ in range(a):
                yield b
    def decompressRLElist(self, A):
        return list(self.solver(A))
