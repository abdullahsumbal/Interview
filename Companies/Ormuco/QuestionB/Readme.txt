class VersionChecker(builtins.object)
 |  A library to compare version
 |
 |  ...
 |
 |  Attributes
 |  ----------
 |  v1 : str
 |      first version (input)
 |  v2 : str
 |      second version (input)
 |
 |  Methods
 |  -------
 |  patternCheck(v1, v2)
 |      Validate pattern of the verion. It should have the following pattern x.x.x
 |      where x can be any number of digits
 |  typeCheck(v)
 |      Validate type. the version input should be a string
 |  compare()
 |      Return the comparsion information for two version.
 |  setV1(v1)
 |      Set version one value
 |  setV2(v1)
 |      Set version two value
 |
 |  Methods defined here:
 |
 |  __init__(self, v1=None, v2=None)
 |      Parameters
 |      ----------
 |      v1 : str
 |          first version (input)
 |      v2 : str
 |          second version (input)
 |
 |  compare(self)
 |      Return comparsion information.
 |      Parameters
 |      ----------
 |
 |      Returns
 |      -------
 |      message: string
 |          comparsion result
 |
 |      Raises
 |      ------
 |      Excepton
 |          If both version are not set
 |
 |  patternCheck(self, v)
 |      Validate pattern of the verion. It should have the following pattern x.x.x
 |      where x can be any number of digits
 |
 |      Parameters
 |      ----------
 |      v: str
 |          version
 |
 |      Returns
 |      -------
 |      corretPattern: Boolean
 |          True if the pattern is correct otherwise False
 |
 |  setV1(self, v1)
 |      Set version 1 input value
 |      Parameters
 |      ----------
 |      v2: str
 |          version 1 input value
 |
 |      Raises
 |      ------
 |      Excepton
 |          if version is not string or has an incorrect pattern
 |
 |  setV2(self, v2)
 |      Set version 2 input value
 |      Parameters
 |      ----------
 |      v2: str
 |          version 2 input value
 |
 |      Raises
 |      ------
 |      Excepton
 |          if version is not string or has an incorrect pattern
 |
 |  typeCheck(self, v)
 |      Validate if the version is inputed in the string type
 |
 |      Parameters
 |      ----------
 |      v: str
 |          version
 |
 |      Returns
 |      -------
 |      isString: Boolean
 |          Return True if the version is string otherwise False
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)


Test Methods defined here:
|
|  setUp(self)
|      Setup a version checker library
|
|  test_1(self)
|      v1 is greater than v2
|
|  test_10(self)
|      Correct version pattern
|
|  test_2(self)
|      v2 is greater than v1
|
|  test_3(self)
|      v2 and v1 are equal.
|
|  test_4(self)
|      v1 not a string
|
|  test_5(self)
|      v2 not a string
|
|  test_6(self)
|      only set version 1 value
|
|  test_7(self)
|      only set version 1 value
|
|  test_8(self)
|      Incorrect version pattern
|
|  test_9(self)
|      Incorrect version pattern
|
