# https://leetcode.com/problems/excel-sheet-column-title/submissions/

class Solution:
    def convertToTitle(self, n: int) -> str:

        column = ""
        while (n != 0):
            temp = n % 26
            if temp == 0:
                n = int(n / 26) - 1
                column = 'Z' + column
            else:
                n = int(n / 26)
                column = chr(temp + 64) + column

        return column

