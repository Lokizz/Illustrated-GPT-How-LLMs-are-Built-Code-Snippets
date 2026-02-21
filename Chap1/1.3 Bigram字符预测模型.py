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
      ngram = tuple(tokens[i:i+n])   # 将 N-Gram 转换为元组
      prefix = ngram[:-1]  # 前缀是 N-Gram 的前 n-1 个元素
      token = ngram[-1]    # 获取 N-Gram 的目标单字
      ngrams_count[prefix][token] += 1  # 更新 N-Gram 计数
  return ngrams_count


#* 4. 定义计算 N-Gram 出现概率的函数
def ngram_probabilities(ngrams_counts):
  ngram_probs = defaultdict(Counter)  # 定义存储 N-Gram 出现概率的字典
  for prefix, tokens_count in ngrams_counts.items():
    total_count = sum(tokens_count.values())  # 计算当前 N-Gram 前缀的总计数
    for token, count in tokens_count.items(): # 遍历每个前缀的 N-Gram
      ngram_probs[prefix][token] = round(count / total_count, 3)  # 计算 N-Gram 出现概率
  return ngram_probs

#* 5. 根据 Bigram 出现的概率，定义生成下一个词的函数
def generate_next_token(prefix, bigram_probs):
  # 如果前缀不在 N-Gram 中，返回 None
  if prefix not in bigram_probs:
    return None
  next_token_probs = bigram_probs[prefix]  # 获取前缀对应的 N-Gram 出现概率
  next_token = max(next_token_probs, key=next_token_probs.get)  # 获取出现概率最高的下一个词
  return next_token

#* 6. 输入一个前缀，生成连续文本
def generate_text(prefix, ngram_probs, n, length=6):
  tokens = list(prefix)  # 将前缀转换为列表
  for _ in range(length):
    next_token = generate_next_token(tuple(tokens[-(n-1):]), ngram_probs)  # 获取下一个词
    if next_token is None:  # 如果没有下一个词，停止生成
      break
    tokens.append(next_token)  # 将下一个词添加到生成的文本中
  return ''.join(tokens)

bigram_counts = count_ngrams(corpus, 2)  # 计算 Bigram 词频
print("Bigram 词频:")
for prefix, counter in bigram_counts.items():
  print(f"{prefix} -> {dict(counter)}")
bigram_probs = ngram_probabilities(bigram_counts)  # 计算 Bigram 出现概率
print("\nBigram 出现概率:")
for prefix, probs in bigram_probs.items():
  print(f"{prefix} -> {dict(probs)}")

# 测试生成文本
prefix = "苹"
generated_text = generate_text(prefix, bigram_probs, n=2, length=6)
print(f"\n输入前缀: '{prefix}' -> 生成文本: '{generated_text}'")