#def loadmod():
import math
MAX_NUM = 100000000
STATUS_NUM = 4
pi = [0.0 for i in range(STATUS_NUM)]
jump_pro = [[0.0 for i in range(STATUS_NUM)] for j in range(STATUS_NUM)]
emi_pro  = [dict() for i in range(STATUS_NUM)]

def loadmod():
    fd = open("md.txt","r",encoding = "utf8")
    
    line = fd.readline()
    pi_str = line.split()
    for i in range(len(pi_str)):
        pi[i] = float(pi_str[i])
    
    for i in range(STATUS_NUM):
        line = fd.readline()
        j_str = line.split()
        for j in range(STATUS_NUM):
            jump_pro[i][j] = float(j_str[j])
    print(jump_pro)
    
    for i in range(STATUS_NUM):
        line = fd.readline()
        e_str = line.split()
        index = 0
        while index < len(e_str):
            emi_pro[i][e_str[index]] = float(e_str[index+1])
            index += 2
        #print(emi_pro)
       
loadmod()

sentence = "这篇文章主要介绍使用Go语言来实现客户端上传文件和服务端处理接收文件的功能"
#sentence = "蓝天、碧水、净土保卫战顺利推进，各项民生事业加快发展，人民生活持续改善。京津冀协同发展、长江经济带发"
#print(len(sentence))
greedy = [[0.0 for i in range(STATUS_NUM)] for j in range(len(sentence))]
greedy_status = [0 for i in range(len(sentence) - 1)]

for i in range(STATUS_NUM):
    if emi_pro[i].get(sentence[0]) is None:
        emi = 0.0 - MAX_NUM
    else: emi = emi_pro[i][sentence[0]]
    p = pi[i]
    if p == 0:
        p = 0.0 - MAX_NUM
    greedy[0][i] = p + emi
#print(greedy)


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
    #print(greedy)
    #print(pi)
    #break;

index = len(sentence) - 1
while index >= 0:
    st = 0
    for i in range(STATUS_NUM):
        if greedy[index][i] > greedy[index][st]:
            st = i
    greedy_status[index] = st
    index -= 1

#print(sentence)
print(greedy_status)
i = 0
s = str()
for ch in sentence:
    if greedy_status[i] == 3 or greedy_status[i] == 2:
        s  = s + ch + ' '
    else :
        s = s+ch
    i += 1
print(s)
    #for i in range(STATUS_NUM):
    #    if index == 0:
    #        max_num = (max_num,pi[i]+emi[i][sentence[index]])
    #    else:
    #        max_num = +emi[i][sentence[index]]
             
                
