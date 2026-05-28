class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}

        for index, value in enumerate(nums):
            res = target - value
            if res in hsh:
                return [hsh[res], index]
        
            hsh[value] = index