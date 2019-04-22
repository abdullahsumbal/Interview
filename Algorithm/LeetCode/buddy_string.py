class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        if len(A) == 0 or len(B) == 0:
            return False

        different_letters = 0
        first_different_letter_A = ""
        first_different_letter_B = ""
        same = 1
        previous = ""

        for A_letter, B_letter in zip(A, B):
            if A_letter != B_letter:
                different_letters += 1
                if different_letters == 1:
                    first_different_letter_A = A_letter
                    first_different_letter_B = B_letter
                elif different_letters == 2 and (
                        first_different_letter_A != B_letter or first_different_letter_B != A_letter):
                    return False
            elif previous == A_letter:
                same += 1

            previous = A_letter

        print(different_letters, same)
        if different_letters == 0 and same < 2:
            return False
        elif different_letters == 1:
            return False
        else:
            return True



if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings("ba", "ba"))