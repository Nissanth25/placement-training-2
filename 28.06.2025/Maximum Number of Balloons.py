class Solution(object):
    def maxNumberOfBalloons(self, text):

        a = ['b', 'a', 'l', 'o', 'n']

        b = [text.count(i) for i in a]

        c = 0

        while True:

            if b[0] >= 1 and b[1] >= 1 and b[2] >= 2 and b[3] >= 2 and b[4] >= 1:

                b = b[0] - 1, b[1] - 1, b[2] - 2, b[3] - 2, b[4] - 1

                c += 1

            else:
                break

        return c
