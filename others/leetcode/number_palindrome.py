
def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    if (x < 0):
        return False
    if(x<10):
        return True
    string = str(x)


    return (string == string[::-1])


if __name__ == '__main__':
    print(isPalindrome(1012))
