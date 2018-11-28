import math
STATUS_NUM = 4
MAX_NUM = 100000000
pi = [0.0 for i in range(STATUS_NUM)]
pi_sum = 0.0

jump_pro = [[0.0 for i in range(STATUS_NUM)] for j in range(STATUS_NUM)]
jump_sum = [0.0 for i in range(STATUS_NUM)]

emi_pro  = [dict() for i in range(STATUS_NUM)]
#emi_sum = dict()
emi_sum = [0.0 for i in range(STATUS_NUM)]

def getlist(word):
    l = []
    for i in range(len(word)):
        l.append(word[i])
    return l
with open('data/allfiles.txt') as fd:
    while True:
        word_status_list = []
        word_list = []
        line = fd.readline()
        if not line:
            break;
        w_list = line.strip()
        for word in w_list.split():
            cur_status_list = [-1 for i in range(len(word))]
            if len(word) == 0:
                continue
            if len(word) == 1:
                cur_status_list[0] = 3
            else:
                cur_status_list[0] = 0
                cur_status_list[-1] = 2
                for i in range(1,len(cur_status_list)-1):
                    cur_status_list[i] = 1
            word_status_list.extend(cur_status_list)
            word_list.extend(getlist(word))
            #print(cur_status_list)
            #print(word)
            #break;

        #print(word_status_list)
        for i in range(len(word_list)):
            status = word_status_list[i]
            ch = word_list[i]
            if i == 0:
               pi[status] += 1
               pi_sum += 1

            if word_list[i] in emi_pro[status]:
               emi_pro[status][ch] += 1
            else:
               emi_pro[status][ch] = 1

            #if word_list[i] im emi_sum.keys():
            #   emi_sum[word_list[i]] += 1
            #else
            #   emi_sum[word_list[i]] = 1
            emi_sum[status] += 1

            if i+1 < len(word_status_list)-1:
                jump_pro[status][word_status_list[i+1]] += 1
                jump_sum[status] += 1
fd = open('md.txt', 'wb')
for i in range(STATUS_NUM):
    if pi[i] > 0:
        pi[i] = math.log(pi[i]/pi_sum)
    else:
        pi[i] = 0
    fd.write((str(pi[i]) + ' ').encode())
fd.write('\n'.encode())

for i in range(STATUS_NUM):
    for j in range(STATUS_NUM):
        if jump_pro[i][j] > 0:
            jump_pro[i][j] = math.log(jump_pro[i][j]/jump_sum[i])
        else:
            jump_pro[i][j] = 0.0
        #if jump_pro[i][j] > 0:
        #    jump_pro[i][j] = math.log(jump_pro[i][j]/jump_sum[i])
        #else:
        #    jump_pro[i][j] = math.log(1.0/MAX_NUM)
        fd.write((str(jump_pro[i][j]) + ' ').encode())
    fd.write('\n'.encode())

for i in range(STATUS_NUM):
    for key in emi_pro[i]:
        emi_pro[i][key] = math.log(emi_pro[i][key]/emi_sum[i])
        fd.write((key + ' ' + str(emi_pro[i][key]) + ' ').encode())
    fd.write('\n'.encode())

fd.close()




