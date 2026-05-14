class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dis = {}
        return_list = []

        # Count frequencies
        for num in nums:

            if num not in dis:
                dis[num] = 0

            dis[num] += 1

        # Find top k
        for i in range(k):

            max_count = 0
            max_key = None

            for key, value in dis.items():

                if value > max_count:
                    max_count = value
                    max_key = key

            return_list.append(max_key)

            del dis[max_key]

        return return_list