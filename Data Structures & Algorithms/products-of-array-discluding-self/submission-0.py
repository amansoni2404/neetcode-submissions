class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_multiples = [0 for i in range(0, len(nums))]
        postfix_multiples = [0 for i in range(0, len(nums))]

        for i in range(0, len(nums)):
            if i == 0:
                prefix_multiples[i] = 1
            else:
                prefix_multiples[i] = prefix_multiples[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postfix_multiples[i] = 1
            else:
                postfix_multiples[i] = postfix_multiples[i+1] * nums[i+1]
        output = []
        for i in range(0,len(nums)):
            result = prefix_multiples[i] * postfix_multiples[i]
            output.append(result)
        return output
        