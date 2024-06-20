class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if not nums[i] in Dict:
                Dict[complement] = i
            else:
                return [Dict[nums[i]], i]
        return None
