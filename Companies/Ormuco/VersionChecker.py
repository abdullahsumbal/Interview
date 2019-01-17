import re

class VersionChecker:
    """
    A library to compare version

    ...

    Attributes
    ----------
    v1 : str
        first version (input)
    v2 : str
        second version (input)

    Methods
    -------
    patternCheck(v1, v2)
        Validate pattern of the verion. It should have the following pattern x.x.x
        where x can be any number of digits
    typeCheck(v)
        Validate type. the version input should be a string
    compare()
        Return the comparsion information for two version.
    setV1(v1)
        Set version one value
    setV2(v1)
        Set version two value
    """

    def __init__(self, v1=None, v2=None):
        """
        Parameters
        ----------
        v1 : str
            first version (input)
        v2 : str
            second version (input)
        """
        self.v1 = v1
        self.v2 = v2

    def patternCheck(self, v):
        """
        Validate pattern of the verion. It should have the following pattern x.x.x
        where x can be any number of digits

        Parameters
        ----------
        v: str
            version

        Returns
        -------
        corretPattern: Boolean
            True if the pattern is correct otherwise False
        """
        corretPattern = True
        m = re.match('^\d+\.\d+\.\d+$|^\d+\.\d+$', v)
        if m == None:
            corretPattern = False
        return corretPattern

    def typeCheck(self, v):
        """
        Validate if the version is inputed in the string type

        Parameters
        ----------
        v: str
            version

        Returns
        -------
        isString: Boolean
            Return True if the version is string otherwise False
        """
        isString = True
        if not isinstance(v, str):
            isString = False
        return isString


    def compare(self):
        """Return comparsion information.
        Parameters
        ----------

        Returns
        -------
        message: string
            comparsion result

        Raises
        ------
        Excepton
            If both version are not set
        """
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
        """Set version 2 input value
        Parameters
        ----------
        v2: str
            version 2 input value

        Raises
        ------
        Excepton
            if version is not string or has an incorrect pattern
        """
        if not self.typeCheck(v2):
            raise Exception('v2 should be a string')
        if not self.patternCheck(v2):
            raise Exception('v2 does not have the correct pattern.')
        self.v2 = v2

    def setV1(self, v1):
        """Set version 1 input value
        Parameters
        ----------
        v2: str
            version 1 input value

        Raises
        ------
        Excepton
            if version is not string or has an incorrect pattern
        """
        if not self.typeCheck(v1):
            raise Exception('v1 should be a string')
        if not self.patternCheck(v1):
            raise Exception('v1 does not have the correct pattern.')
        self.v1 = v1
