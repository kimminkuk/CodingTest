def solution(skill, skill_trees):
    answer = 0
    for key in skill_trees:
        s_iter = 0
        temp = False
        for j in range(0, len(key)):
            if  key[j] in skill:
                temp = True
                if key[j] == skill[s_iter]:
                    s_iter += 1
                    if s_iter == len(skill):
                        break
                else:
                    s_iter = 0
                    break
                
                
                # if not key[j] == skill[s_iter]:
                #     s_iter = 0
                #     break
                # else:
                #     s_iter+=1
        if s_iter > 0 or temp == False:
            answer+=1
    return answer
