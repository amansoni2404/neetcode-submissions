class Solution:
    def getDigitSum(self, number):
        sum = 0
        while number != 0:
            digit = number % 10
            number = number // 10
            sum = sum + pow(digit, 2)
        return sum

    def isHappy(self, n: int) -> bool:
        stored_sum = set()
        squared_sum = self.getDigitSum(n)
        while squared_sum not in stored_sum:
            if squared_sum == 1:
                return True
            else:
                stored_sum.add(squared_sum)
            squared_sum = self.getDigitSum(squared_sum)
        return False
        
        