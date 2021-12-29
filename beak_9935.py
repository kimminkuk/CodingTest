def sol(arrOri, arrBomb):
    answer =''
    arrOri_len = len(arrOri)
    arrBomb_len = len(arrBomb)
    s_iter = 0
    j = 0
    while True:
        print('j=> ', j)
        if arrBomb[s_iter] == arrOri[j]:
            if s_iter == arrBomb_len-1:
                temp = j - (arrBomb_len-1)
                arrOri = arrOri[:temp] + arrOri[j+1:]
                print('temp=> ', temp, 'arrOri=> ', arrOri)
                arrOri_len = len(arrOri)
                s_iter = 0
                j = 0
            else:
                s_iter += 1
        else :
            s_iter = 0
        j += 1
        if arrOri_len <= j:
            break
    answer = arrOri
    return answer


test = str(input())
test2 = str(input())

result = sol(test, test2)
print(result)
