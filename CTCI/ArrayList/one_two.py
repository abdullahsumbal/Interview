


def checkPermutation(s1, s2):
    s1Array = [0] * 128
    s1Length = len(s1)
    s2Length = len(s2)

    if s1Length != s2Length:
        return False

    for i in range(s1Length):
        s1Array[ord(s1[i])]  += 1


    for i in range(s2Length):
        s1Array[ord(s2[i])] -= 1
        if(s1Array[ord(s2[i])] < 0):
            return False

    return True

if __name__ == '__main__':
    string1 = "abccdf"
    string2 = "abccdf"
    print(checkPermutation(string1, string2))
