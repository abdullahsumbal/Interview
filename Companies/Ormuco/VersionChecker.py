import re

class VersionChecker:

    def __init__(self, v1=None, v2=None):
        self.v1 = v1
        self.v2 = v2

    def patternCheck(self, v):
        m = re.match('^\d+\.\d+\.\d+$|^\d+\.\d+$', v)
        if m == None:
            return False
        return True

    def typeCheck(self, v):
        if not isinstance(v, str):
            return False
        return True


    def compare(self):

        # check if both version are set
        if self.v1 == None:
            raise Exception('Please set version 1 value.')
        if self.v2 == None:
            raise Exception('Please set version 2 value.')

        # comapre
        message = ""
        if self.v1 > self.v2:
            message = "v1 is greater than v2."
        elif self.v2 > self.v1:
            message = "v2 is greater than v1."
        else:
            message = "v2 and v1 are equal."

        return message

    def setV2(self, v2):
        if not self.typeCheck(v2):
            raise Exception('v2 should be a string')
        if not self.patternCheck(v2):
            raise Exception('v2 does not have the correct pattern.')
        self.v2 = v2

    def setV1(self, v1):
        if not self.typeCheck(v1):
            raise Exception('v1 should be a string')
        if not self.patternCheck(v1):
            raise Exception('v1 does not have the correct pattern.')
        self.v1 = v1
