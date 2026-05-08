class Solution:

    def digit_sum(self, num):
        sum = 0
        while (num != 0):
            digit = num % 10
            num = num // 10
            sum = sum + pow(digit , 2)
        return sum

    def isHappy(self, n: int) -> bool:
        sum = self.digit_sum(n)
        sum_set = set()
        while sum not in sum_set:
            if sum == 1:
                return True
            else:
                sum_set.add(sum)
                sum = self.digit_sum(sum)
        return False

        