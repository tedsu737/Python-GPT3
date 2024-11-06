import jieba
from collections import Counter

chinese_sentence = [
    '今天下午進行芯愛利潤最大化的方案規劃討論會',
    '川普當選美國總統',
    '中和辦公室的租金為一萬五千元',
    '台北下雨了',
    '這個週末要團練'
]

vocab = [] # 分析文本後產生的詞彙表
for sentence in chinese_sentence:
	# tokens = sentence.split(' ') # 空白斷詞產生token
    tokens = jieba.lcut(sentence)
    vocab.extend(tokens)
    #print(tokens)
    #input()
    # vocab.extend(tokens) 
	
vocab = sorted(set(vocab)) # 通過set()過濾重複單字，並用sorted()進行排序
print(vocab)