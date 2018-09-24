#-*- coding:utf-8 -*- 


def get_LCS_sequence(sentenceA,sentenceB):
        width = len(sentenceA)
        length = len(sentenceB)

        matrix = list()
        for i in range(width):
                l = [0 for n in range(length)]
                matrix.append(l)
        max_match = 0
        for i in range(length):
                for j in range(width):
                        if sentenceA[j] == sentenceB[i]:
                                for index in range(j:width):
                                        matrix[i][index] = marmax_match + 1
                                        break;
                        matrix[i][j] = max_match


        return matrix







if __name__ == "__main__":
        print(get_LCS_sequence('abcdd', 'bcdb'))
