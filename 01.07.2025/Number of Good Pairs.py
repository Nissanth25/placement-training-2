class Solution(object):
    def numIdenticalPairs(self, nums):
        count_map = {}
        total_pairs = 0

        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        for count in count_map.values():
            if count > 1:
                total_pairs += (count * (count - 1)) // 2

        return total_pairs
