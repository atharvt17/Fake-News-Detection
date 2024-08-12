# news_detection/preprocessing.py
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

# You need to implement the preprocess_text function based on your preprocessing steps used during training
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    return text