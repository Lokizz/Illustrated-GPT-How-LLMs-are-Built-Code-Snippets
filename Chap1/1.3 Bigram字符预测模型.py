"""
* Steps:
- 1. 构建实验语料库；
- 2. 把句子分成 N个 Gram（分词）
- 3. 计算每个 Bigram 在语料库中的词频
- 4. 计算每个 Bigram 的出现概率
- 5. 根据 Bigram 出现的概率，定义生成下一个词的函数
- 6. 输入一个前缀，生成连续文本
"""
from collections import defaultdict, Counter

#* 1. 构建语料库
# 构建一个玩具数据集
corpus = [ "我喜欢吃苹果",
        "我喜欢吃香蕉",
        "她喜欢吃葡萄",
        "他不喜欢吃香蕉",
        "他喜欢吃苹果",
        "她喜欢吃草莓"]

#* 2. 把句子分成 N个 Gram（分词）
# 定义一个分词函数
def tokenize(text):
  return [char for char in text]  # 将文本拆分为字符列表

# tokenize 函数测试
# for cor in corpus:
#   print(tokenize(cor))

#* 3. 计算每个 Bigram 在语料库出现的词频
def count_ngrams(corpus, n):
  #- 创建存储 N-gram 计算的字典
  ngrams_count = defaultdict(Counter)

  for text in corpus:
    tokens = tokenize(text)  # 对文本进行分词
    for i in range(len(tokens) - n + 1): #! 遍历分词结果, 生成 N-Gram
      ngram = tuple(tokens[i:i+n])   #! 将 N-Gram 转换为元组
      prefix = ngram[:-1]  #! 前缀是 N-Gram 的前 n-1 个元素
      token = ngram[-1]    #! 获取 N-Gram 的目标单字
      ngrams_count[prefix][token] += 1  #! 更新 N-Gram 计数
  return ngrams_count

bigram_counts = count_ngrams(corpus, 2)  # 计算 Bigram 词频
print("Bigram 词频:")
for prefix, counter in bigram_counts.items():
  print(f"{prefix} -> {dict(counter)}")