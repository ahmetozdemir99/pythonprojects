
def read_numbers(filename_):
    if not ('.' in filename_):
        filename_ = filename_ + '.txt'
    infile = open(filename_, 'r')
    lines = infile.readlines()
    S_ = []
    for i in lines:
        line = i.split()
        line1 = []
        for j in line:
            line1.append(int(j))
        S_.append(line1)
    return S_


""" MAIN CODE"""


""" copy the lines above and continue below """


def findMulpArray(array,start,end):
    result = 1
    returnedArray = []
    for i in array[start:end + 1]:
        result *= i
        returnedArray.append(i)
    return [result,returnedArray]





def verticalChecker(array,length):
    max = 1
    resultArray = []
    for i in range(len(array) - length + 1):
        for j in range(len(array[i]) - length + 1):
            result = 1
            resultArray2 = []
            for k in range(length):
                result *= array[i + k][j]
                resultArray2.append(array[i + k][j])
            if result > max:
                max = result
                resultArray = [i , j , "south", resultArray2, max]
    return resultArray


def horizontalChechker(array,length):
    max = 1
    resultArray = []
    rowCounter = 0
    for i in array:
        start = 0
        end = length - 1
        columnCounter = 0
        while(end <= len(i) + 1):
            result = findMulpArray(i,start,end)[0]
            if(result > max):
                max = result
                resultArray = [rowCounter + 1 ,columnCounter + 1,"east", findMulpArray(i,start,end)[1],max]
            start += 1
            end += 1
            columnCounter += 1
        rowCounter += 1
    return resultArray



def çaprazBul2(array, length): #
    max = 1
    resultArray = []
    for i in range(len(array) - length + 1):
        for j in range(len(array[i]) - length + 1):
            result = 1
            resultArray2 = []
            for k in range(length):
                result *= array[i + k][j + k]
                resultArray2.append(array[i + k][j + k])
            if result > max:
                max = result
                resultArray = [i + 1, j + 1,"southeast",resultArray2, max]
    return resultArray





def reverseArray(array):
    reversedArray = [row for row in array[::-1]]
    return reversedArray


def console(filename, k, max, numbers, i, j, direction ):
    print("Input file: ",filename)
    print("Length: ", k)
    print("The greatest product: ", max)
    print("Numbers: ", numbers)
    print("Location: i=",i, " , j=",j )
    print("Direction: ", direction)








def main():
    maxList = [horizontalChechker(S,k)[4], çaprazBul2(S,k)[4], çaprazBul2(reverseArray(S),k)[4], verticalChecker(S,k)[4]] # 0 -> east , 1 southeast, 2 south west, 3 south
    if(max(maxList) == maxList[0]):
        console(filename,k,horizontalChechker(S,k)[4], horizontalChechker(S,k)[3],horizontalChechker(S,k)[0],horizontalChechker(S,k)[1],horizontalChechker(S,k)[2])
        print()
        print()
        print(horizontalChechker(S,k))
    elif(max(maxList) == maxList[1]):
        console(filename,k,çaprazBul2(S,k)[4], çaprazBul2(S,k)[3],çaprazBul2(S,k)[0],çaprazBul2(S,k)[1],çaprazBul2(S,k)[2])
        print()
        print()
        print(çaprazBul2(S,k))
    elif(max(maxList) == maxList[3]):
        console(filename,k,verticalChecker(S,k)[4], verticalChecker(S,k)[3],verticalChecker(S,k)[0], verticalChecker(S,k)[1],verticalChecker(S,k)[2])
        print()
        print()
        print(verticalChecker(S,k))
    else:
        returnedList = çaprazBul2(reverseArray(S),k)
        x = returnedList[0]
        y = returnedList[1]
        returnedList[0] = y
        returnedList[1] = len(S[0])- x + 1
        returnedList[2] = "southwest"
        returnedList[3].reverse()
        console(filename,k,returnedList[4], returnedList[3],returnedList[0],returnedList[1],returnedList[2])
        print()
        print()
        print(returnedList)



filename = input('Enter the name of the txt file : ')
k = int(input('Enter the # of the numbers to be multiplied : '))
S = read_numbers(filename)
