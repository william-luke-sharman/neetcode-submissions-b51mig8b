class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1

        res = list(res.items())
        res = sorted(res, key=lambda tup: tup[1], reverse=True)
        res = [tup[0] for tup in res]
        return res[:k]