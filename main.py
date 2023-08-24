class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {value:index for index, value in enumerate(nums)}
        for i in range(len(nums)):
            diff = target-nums[i]
            if d.get(diff, False) and d[diff]!=i:
                return [i, d[diff]]
