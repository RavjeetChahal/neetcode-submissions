class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        res = []
        for num in nums:
            mp[num] += 1

        for i in range(k):
            res.append(max(mp, key=mp.get))
            mp.pop(max(mp, key=mp.get))

        return res