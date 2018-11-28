import math
from comm import MAX_NUM
from comm import STATUS_NUM
from comm import pi
from comm import jump_pro
from comm import emi_pro
from comm import loadmod
from comm import splitsent
loadmod()

def greedy_segment(sentence):
    greedy = [[0.0 for i in range(STATUS_NUM)] for j in range(len(sentence))]
    greedy_status = [0 for i in range(len(sentence))]
    
    for i in range(STATUS_NUM):
        if emi_pro[i].get(sentence[0]) is None:
            emi = 0.0 - MAX_NUM
        else: emi = emi_pro[i][sentence[0]]
        p = pi[i]
        if p == 0:
            p = 0.0 - MAX_NUM
        greedy[0][i] = p + emi
    
    
    for index in range(1,len(sentence)):
        for i in range(STATUS_NUM):
            if emi_pro[i].get(sentence[index]) is None:
                emi = 0.0 - MAX_NUM
            else:
                emi = emi_pro[i][sentence[index]]
            max_num = None
            for j in range(STATUS_NUM):
                if jump_pro[j][i] == 0:
                    jump = 0.0 - MAX_NUM
                else:
                    jump = jump_pro[j][i]
                if max_num == None: max_num = greedy[index-1][j] + emi + jump
                else: max_num = max(max_num,greedy[index-1][j] + emi + jump)
            greedy[index][i] = max_num
    
    index = len(sentence)
    for i in range(index):
        if i == 0:
            best_status = 3 if greedy[i][0] < greedy[i][3] else 0 
        else:
            best_status = 0
            for s in range(STATUS_NUM):
                pre_status = greedy_status[i - 1]
                if pre_status == 0 or pre_status == 1:
                    best_status = 1 if greedy[i][1] > greedy[i][2] else  2
                else:
                    best_status = 3 if greedy[i][0] < greedy[i][3] else 0 
            
        greedy_status[i] = best_status
                
    print(greedy_status)

    return splitsent(greedy_status, sentence)
             
if __name__ == "__main__":                
    sentence = "这篇文章主要介绍使用Go语言来实现客户端上传文件和服务端处理接收文件的功能"
    #sentence = "蓝天、碧水、净土保卫战顺利推进，各项民生事业加快发展，人民生活持续改善。京津冀协同发展、长江经济带发"
    print(greedy_segment(sentence))
