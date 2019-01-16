#Question B

# The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
import unittest

class VersionChecker:

    def __init__(self, v1=None, v2=None):
        self.v1 = v1
        self.v2 = v2

    def compare(self):
        if self.v1 == None:
            raise Exception('Please set version 1 value.')
        if self.v2 == None:
            raise Exception('Please set version 2 value.')

        message = ""
        if self.v1 > self.v2:
            message = "v1 is greater than v2."
        elif self.v2 > self.v1:
            message = "v2 is greater than v1."
        else:
            message = "v2 and v1 are equal."

        return message

    def setV2(self, v2):
        if not isinstance(v2, str):
            raise Exception('v2 should be a string')
        self.v2 = v2

    def setV1(self, v1):
        if not isinstance(v1, str):
            raise Exception('v1 should be a string')
        self.v1 = v1

class TestVersion(unittest.TestCase):

    def setUp(self):
        """
        Setup a version checker library
        """
        self.vChecker = VersionChecker()

    def test_1(self):
        """
        v1 is greater than v2
        """
        self.vChecker.setV1("1.2")
        self.vChecker.setV2("1.1")
        self.assertEqual(self.vChecker.compare(), "v1 is greater than v2.", "v1 should be greater than v2")

    def test_2(self):
        """
        v2 is greater than v1
        """
        self.vChecker.setV1("1.1")
        self.vChecker.setV2("1.2")
        self.assertEqual(self.vChecker.compare(), "v2 is greater than v1.", "v2 should be greater than v1")

    def test_3(self):
        """
        v2 and v1 are equal.
        """
        self.vChecker.setV1("1.1")
        self.vChecker.setV2("1.1")
        self.assertEqual(self.vChecker.compare(), "v2 and v1 are equal.", "v2 and v1 should be equal.")

    def test_4(self):
        """
        v1 not a string
        """
        with self.assertRaises(Exception) as context:
            self.vChecker.setV1(1.1)
            self.vChecker.setV2("1.1")

        self.assertTrue('v1 should be a string' in str(context.exception))

    def test_5(self):
        """
        v2 not a string
        """
        with self.assertRaises(Exception) as context:
            self.vChecker.setV2(1.1)

        self.assertTrue('v2 should be a string' in str(context.exception))

    def test_6(self):
        """
        only set version 1 value
        """
        # self.vChecker = VersionChecker()
        with self.assertRaises(Exception) as context:
            self.vChecker.setV1("1.1")
            self.vChecker.compare()

        self.assertTrue("Please set version 2 value." in str(context.exception))

    def test_7(self):
        """
        only set version 1 value
        """
        # self.vChecker = VersionChecker()
        with self.assertRaises(Exception) as context:
            self.vChecker.setV2("1.1")
            self.vChecker.compare()

        self.assertTrue("Please set version 1 value." in str(context.exception))

if __name__ == '__main__':
    unittest.main()
