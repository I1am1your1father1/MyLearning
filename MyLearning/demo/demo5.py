# Simply show Word2Vec
from gensim.models import Word2Vec

sentences = [["自然", "语言", "处理"], ["预训练", "模型", "很强大"]]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)
print(model.wv["自然"])