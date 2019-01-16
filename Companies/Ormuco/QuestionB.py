#Question B

# The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
import unittest

class StringTest:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def Compare_V1_to_V2(self):
        message = ""
        if self.v1 > self.v2:
            message = "v1 is greater than v2."
        elif self.v2 > self.v1:
            message = "v2 is greater than v1."
        else:
            message = "v2 and v1 are equal."

        return message
        
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
