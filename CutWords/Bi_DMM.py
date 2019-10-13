#-*- coding: utf-8 -*-

'''
双向最大匹配算法
'''
from CutWords import MM,RMM

class BiDMM(object) :
    def __init__(self):
        self.window_size = 3

    def mm_cut(self, text):
        result = []
        index = 0
        text_length = len(text)
        dic = ['研究','研究生','生命','命','的', '起源']
        while text_length > index:
            for size in range(self.window_size+index, index, -1):
                piece = text[index:size]
                if piece in dic:
                    index = size-1
                    result.append(piece + "----")
                    break
            index = index + 1
        return result

    def rmm_cut(self, text):
        result = []
        index = len(text)
        dic = ['研究', '研究生', '生命', '命', '的', '起源']
        while index > 0:
            for size in range(index - self.window_size, index):
                piece = text[size:index]
                if piece in dic:
                    index = size + 1
                    result.append(piece + "----")
                    break
            index = index - 1
        result.reverse()
        return result

    def count(self, List):
        cnt = 0
        for i in List:
            if len(i) == 1:
                cnt = cnt + 1
        return cnt

    def bi_dmm_cut(self, text):
        text = text
        result_mm = self.mm_cut(text)
        result_rmm = self.rmm_cut(text)

        if len(result_mm) < len(result_rmm):
            print(result_mm)
        elif len(result_mm) > len(result_rmm):
            print(result_rmm)
        elif result_mm == result_rmm:
            print(result_mm)  #分词结果相同，无歧义
        elif self.count(result_mm) < self.count(result_rmm):
            print(result_mm)
        else:
            print(result_rmm)

if __name__ == "__main__":
    text = "研究生命的起源"
    tokenizer = BiDMM()
    print(tokenizer.mm_cut(text))
    print(tokenizer.rmm_cut(text))
    print(tokenizer.bi_dmm_cut(text))
    tokenizer.bi_dmm_cut(text)
