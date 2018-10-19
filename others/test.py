import re


def swap(l, i, j):
    tmp = l[j]
    l[j] = i
    l[i] = tmp

string = "10.++*32.7"
string = string.replace(".","a")

list = re.split('([+-/*])', string)
##number_or_symbol = re.compile('(\d+|[^ 0-9])')
#list = re.findall(number_or_symbol, string)
print(list)

left = 0
right = len(list) -1
while(left < right):
    tmp = list[left]
    list[left] = list[right]
    list[right] = tmp
    left = left + 1
    right = right -1






print((("").join(list)).replace("a","."))

print("fdsf".replace("h","d"))


def reverse(expression):
    if(expression == ""):
        return expression
    expression = expression.replace(".","a")
    splitList = re.split("([+-/*])", expression)
    leftIndex = 0;
    rightIndex = len(splitList) -1

    while(leftIndex < rightIndex):
        temp = splitList[leftIndex]
        splitList[leftIndex] = splitList[rightIndex]
        splitList[rightIndex] = temp
        leftIndex = leftIndex + 1
        rightIndex = rightIndex - 1

    newExp = "".join(splitList)
    return newExp.replace("a",".")
