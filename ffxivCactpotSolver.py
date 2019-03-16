
def getNumberOfFilledBlock(ticNumArr):
    count = 0
    for index in ticNumArr:
        if index!=0:
            count=count+1
    return count

def getUsedNumber(ticNumArr):
    result = []
    for index in ticNumArr:
        if index!=0:
            result.append(index)
    return result

def getUnusedNumber(ticNumArr):
    result=list(range(1,10))
    for index in ticNumArr:
        if index != 0:
            result.remove(index)
    return result

def evalArr(ticNumArr):
    for index in range(9):
        ticNumArr[index]=int(ticNumArr[index])
    return ticNumArr

def strArr(combination):
    for index in range(3):
        combination[index]=str(combination[index])
    return combination

def outputBestGainAndCombination(dict):
    print("选择"+list(dict.keys())[list(dict.values()).index(max(list(dict.values())))])
    print("可获得平均最大收益的数学期望为")
    print(max(list(dict.values())))



def calculate(ticNumArr):
    ticNumArr=evalArr(ticNumArr)
    usedNumber=getUsedNumber(ticNumArr)
    unusedNumber=getUnusedNumber(ticNumArr)
    needGuess=[]

    for combination in possibleCombinations:
        #ticNumArr=ticketNumberArray
        for index in combination:
            if ticNumArr[index-1]==0:
                needGuess.append(index)
        if len(needGuess)==0:
            #all the numbers in this condition are clear.
            #so, the result is fixed.
            result = 0
            result=ticNumArr[combination[0]-1]+ticNumArr[combination[1]-1]+ticNumArr[combination[2]-1]
            finalResult[' '.join(strArr(combination))]=gain[result]
        elif len(needGuess)==1:
            results = []
            for index in unusedNumber:
                sum=0
                ticNumArr[needGuess[0]-1]=index
                sum=ticNumArr[int(combination[0])-1]+ticNumArr[int(combination[1])-1]+ticNumArr[int(combination[2])-1]
                results.append(sum)
                sum=0
                for result in results:
                    sum+=gain[result]/5
                finalResult[' '.join(strArr(combination))]=sum/len(results)
        elif len(needGuess)==2:
            result={}
            for firstNumber in unusedNumber:
                for secondNumber in unusedNumber:
                    if firstNumber != secondNumber:
                        ticNumArr[needGuess[0]-1]=firstNumber
                        ticNumArr[needGuess[1]-1]=secondNumber
                        sum=0
                        sum = ticNumArr[int(combination[0]) - 1] + ticNumArr[int(combination[1]) - 1] + ticNumArr[
                            int(combination[2]) - 1]
                        result[gain[sum]]=result[gain[sum]]+1 if result[gain[sum]] else 1
            expectGain=0
            for key in list(result.keys()):
                expectGain+=key*result[key]/400
                finalResult[' '.join(strArr(combination))] = expectGain
        elif len(needGuess)==3:
            result={}
            for firstNumber in unusedNumber:
                for secondNumber in unusedNumber:
                    for thirdNumber in unusedNumber:
                        if firstNumber!=secondNumber and firstNumber!=thirdNumber and secondNumber!=thirdNumber:
                            ticNumArr[needGuess[0]-1]=firstNumber
                            ticNumArr[needGuess[1]-1]=secondNumber
                            ticNumArr[needGuess[2]-1]=thirdNumber
                            sum=0
                            sum = ticNumArr[int(combination[0]) - 1] + ticNumArr[int(combination[1]) - 1] + ticNumArr[
                                int(combination[2]) - 1]
                            try:
                                result[gain[sum]]
                            except KeyError:
                                result[gain[sum]] = 1
                            else:
                                result[gain[sum]] = result[gain[sum]] + 1
            expectGain = 0
            for key in list(result.keys()):
                expectGain += key * result[key] / 3600
                finalResult[' '.join(strArr(combination))] = expectGain
    outputBestGainAndCombination(finalResult)



if __name__ == '__main__':
    possibleCombinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    gain = {
        6: 10000,
        7: 36,
        8: 720,
        9: 360,
        10: 80,
        11: 252,
        12: 108,
        13: 72,
        14: 54,
        15: 180,
        16: 72,
        17: 180,
        18: 119,
        19: 36,
        20: 306,
        21: 1080,
        22: 144,
        23: 1800,
        24: 3600
    }
    finalResult = {}
    ticketNumberArray = "0 9 8 7 0 0 0 2 0".split()
    calculate(ticketNumberArray)



