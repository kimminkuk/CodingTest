#fail

def sol(arr):
    arrSort = sorted(arr, reverse=False)
    arrSort = list(map(str,arrSort))
    arrSort_len = len(arrSort)
    #print(arrSort)

    for i in range(0, arrSort_len-1):
        aSFL=len(arrSort[i])
        if arrSort[i][:aSFL] == arrSort[i+1][:aSFL]:
            answer = 'NO'
            return answer

    answer = 'YES'
    return answer

testNum = int(input())
result = []
test = []
for i in range(0, testNum):
    testNum2 = int(input())
    for j in range(0, testNum2):
        test.append(int(input()))
    result.append(sol(test))
    test.clear()
for i in result:
    print(i)

    
#why...
import sys
input = sys.stdin.readline
def sol(arr):
    arrSort = sorted(arr, reverse=False)
    arrSort = list(map(str,arrSort))
    arrSort_len = len(arrSort)
    #print(arrSort)

    for i in range(0, arrSort_len-1):
        aSFL=len(arrSort[i])
        #print('i->',i,'arr_left: ',arrSort[i], 'arr_right',arrSort[i+1][:aSFL])
        if arrSort[i] == arrSort[i+1][:aSFL]:
            answer = 'NO'
            return answer

    answer = 'YES'
    return answer

testNum = int(input())
for i in range(0, testNum):
    testNum2 = int(input())
    test = []
    for j in range(0, testNum2):
        #test.append(int(input()))
        #test.append(input())
        test.append(input().strip())
    print(sol(test))
