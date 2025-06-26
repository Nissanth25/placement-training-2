class Solution(object):
    def distributeCandies(self, candies, num_people):

        answer = [0] * num_people
        pointer = 0
        giveCandy = 1

        while candies > 0:

            if giveCandy > candies:
                giveCandy = candies
            answer[pointer] += giveCandy
            candies -= giveCandy
            giveCandy += 1
            pointer += 1

            if pointer == num_people:
                pointer = 0

        return answer

        
