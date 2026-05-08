class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if all(values == 0 for values in nums):
            return [[0,0,0]]
        nums_map = {}
        result = set()
        for index, value in enumerate(nums):
            nums_map[value] = index
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                desired = -nums[i]-nums[j]
                if desired in nums_map and nums_map[desired] != i and nums_map[desired] != j:
                    result.add(tuple(sorted([nums[i], nums[j], desired])))        
        return list(result)
        