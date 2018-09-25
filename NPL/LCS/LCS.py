#-*- coding:utf-8 -*- 


def get_LCS_sequence(sentenceA,sentenceB):
        width = len(sentenceA)
        length = len(sentenceB)

        matrix = list()
        for i in range(width):
                l = [0 for n in range(length)]
                matrix.append(l)
                
        for i in range(length):
                for j in range(width):
                        up_pos = 0
                        left_pos = 0
                        parent_pos = 0
                        max_match = 0

                        if j - 1 > 0:
                                up_pos = matrix[j-1][i]
                        if i - 1 > 0:
                                left_pos = matrix[j][i-1]

                        if i - 1 > 0 and j - 1 > 0:
                                parent_pos = matrix[j-1][i-1]

                        if sentenceA[j] == sentenceB[i]:
                                max_match = max(up_pos, left_pos, parent_pos + 1)
                        else:
                                max_match = max(up_pos, left_pos)

                        matrix[j][i] = max_match

        return matrix



if __name__ == "__main__":
        print(get_LCS_sequence('abcdd', 'bcdb'))
