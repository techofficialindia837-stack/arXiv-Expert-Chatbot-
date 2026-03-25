from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# better model
generator = pipeline("text-generation", model="gpt2")

# train
def train_model(df):
    corpus = df['summary'].tolist()
    X = vectorizer.fit_transform(corpus)
    return X, corpus

# search
def search(query, X, corpus):
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, X).flatten()
    idx = scores.argmax()
    return corpus[idx]

# generate
def generate_answer(context, query):
    prompt = f"""
You are an expert AI assistant.
Explain the concept clearly and simply.

Question: {query}

Context: {context}
"""

    result = generator(
        prompt,
        max_new_tokens=120,
        temperature=0.7
    )

    return result[0]['generated_text']

# chatbot
def chatbot(query, X, corpus):
    context = search(query, X, corpus)
    answer = generate_answer(context, query)
    return answer, context