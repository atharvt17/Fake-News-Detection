# news_detection/models.py

#from sklearn.feature_extraction.text import TfidfVectorizer
import os
import joblib
import pickle
class FakeNewsModel:
    @staticmethod
    def rfload():
        model_path = os.path.join(os.path.dirname(__file__), 'log_model')
        model=joblib.load(model_path)
        #model = pickle.load(open(model_path,'rb'))
        return model
    @staticmethod
    def tfload():
        tfidf_path = os.path.join(os.path.dirname(__file__), 'tf_model')
        tfidf_vectorizer=joblib.load(tfidf_path)
        #tfidf_vectorizer = pickle.load(open(tfidf_path,'rb'))
        return tfidf_vectorizer
