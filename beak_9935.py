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




# def sol(arr, arrSearch):
#     answer = ''
#     stk = []
#     arr_len = len(arr)
#     arrSearch_len = len(arrSearch)
#     for i in range(0, arr_len):
#         stk.append(arr[i])
#         if arr[i] == arrSearch[-1]:
#             temp = ''.join(stk[len(stk)-arrSearch_len:])
#             if temp == arrSearch:
#                 for j in range(0, arrSearch_len):
#                     stk.pop()
#     answer = stk
#     return answer

# arr = []
# arr = str(input())
# arrSearch = str(input())
# result = sol(arr, arrSearch)
# print(result)
