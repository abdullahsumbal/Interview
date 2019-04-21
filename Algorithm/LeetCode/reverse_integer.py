# problem: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        max_integer = pow(2, 31) - 1
        min_integer = - pow(2, 31)

        if -10 < x < 10:
            return x

        isNegative = False
        if x <= -10:
            x *= -1
            isNegative = True

        reverse = 0
        while (x >= 10):
            reverse += (x % 10)
            reverse = reverse * 10
            x = int(x / 10)

        reverse += x

        if max_integer < reverse:
            return 0

        if min_integer > reverse:
            return 0


        if isNegative:
            reverse *= -1
        return reverse

# can not deal with overflow
class Solution1:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x

        isNegative = False
        if x <= -10:
            x *= -1
            isNegative = True

        reverse = 0
        while (x >= 10):
            reverse += (x % 10)
            reverse = reverse * 10
            x = int(x / 10)

        reverse += x

        if isNegative:
            reverse *= -1
        return reverse


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(pow(2, 31)))
