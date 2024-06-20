class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in Dict:
                return [Dict[nums[i]], i]
            else:
                Dict[complement] = i
        return None
