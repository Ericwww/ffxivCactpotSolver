# ffxivCactpotSolver
Calculate the best solve of the FinalFantasyXIV Cactpot on Python
## Usage
As it says
## Introduction
利用数学期望来计算
当遍历数组计算出多个收益值时，会取平均数来反映此情况下的最大收益

当一行里有一个数字不知道时
```python
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
```
默认每个数字出现的概率是等概的，故此处sum/5，可得对应的数学期望

当一行里有两个数字不知道时
```
result={}
    for firstNumber in unusedNumber:
        for secondNumber in unusedNumber:
            if firstNumber != secondNumber:
                ticNumArr[needGuess[0]-1]=firstNumber
                ticNumArr[needGuess[1]-1]=secondNumber
                sum=0
                sum = ticNumArr[int(combination[0]) - 1] + ticNumArr[int(combination[1]) - 1] + ticNumArr[int(combination[2]) - 1]
                try:
                    result[gain[sum]]
                except KeyError:
                    result[gain[sum]] = 1
                else:
                    result[gain[sum]] = result[gain[sum]] + 1
    expectGain=0
    for key in list(result.keys()):
        expectGain+=key*result[key]/400
        finalResult[' '.join(strArr(combination))] = expectGain
```
两个数字出现的概率变为1/20，又因为会得到20个结果，故expectGain/400

三个数字不知道时更是同理
```python
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
```