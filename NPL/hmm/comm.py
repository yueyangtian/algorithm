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
    
    for i in range(STATUS_NUM):
        line = fd.readline()
        e_str = line.split()
        index = 0
        while index < len(e_str):
            emi_pro[i][e_str[index]] = float(e_str[index+1])
            index += 2
def splitsent(status, sentence):
    i = 0
    s = str()
    for ch in sentence:
        if status[i] == 3 or status[i] == 2:
            s  = s + ch + ' '
        else :
            s = s+ch
        i += 1
    return s
