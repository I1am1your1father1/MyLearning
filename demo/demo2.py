# A extremely simple demo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

data = [
    {"text": "比尔盖茨是微软的创始人", "relations": [{"head": "比尔盖茨", "tail": "微软", "type": "创始人"}]},
    {"text": "北京是中国的首都", "relations": [{"head": "北京", "tail": "中国", "type": "首都"}]}
]

texts = [d["text"] for d in data]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

y = [d["relations"][0]["type"] for d in data]  
model = SVC()
model.fit(X, y)

test_text = "乔布斯创立了苹果公司"
test_vec = vectorizer.transform([test_text])
prediction = model.predict(test_vec)
print(f"预测关系: {prediction[0]}")