import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

titles = [
    "苹果 发布 新款iPhone手机",
    "苹果公司 推出 新款智能手机",
    "微软 公布 季度财报",
    "谷歌 宣布 新的人工智能计划"
]

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(titles)
similarities = cosine_similarity(tfidf_matrix)

df = pd.DataFrame(similarities, columns=titles, index=titles)
print(df)