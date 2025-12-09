import os
import nltk
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()
vectorizer = TfidfVectorizer()

#CSV path to avoid crash
csv_path = os.path.join(
    os.path.dirname(__file__),
    "dataset",
    "faq_dataset.csv"
)

faq_data = pd.read_csv(csv_path ,index_col=False)

questions = faq_data["question"].tolist()
answers = faq_data["answer"].tolist()


# Preprocessing function
def clean_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens  = [t for t in tokens if t not in stopwords.words('english')]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)

#select the best answer function
def get_best_answer(user_input , return_score=False):
    user_input_clean = clean_text(user_input)
    user_vec = vectorizer.transform([user_input_clean])
    similarity_scores = cosine_similarity(user_vec, faq_vectors)
    best_idx = similarity_scores.argmax()
    score = similarity_scores.max()

    if score < 0.2:
        answer = "Sorry, I don't understand your question."
    else:
        answer = answers[best_idx]
    
    if return_score:
        return answer
    return answer



# Train vectorizer once
clean_questions = [clean_text(q) for q in questions]
faq_vectors = vectorizer.fit_transform(clean_questions)