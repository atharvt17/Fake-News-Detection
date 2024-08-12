# news_detection/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import FakeNewsModel
from .preprocessing import preprocess_text

def index(request):
    return render(request, 'index.html')

def analyze_article(request):
    if request.method == 'POST':
        news_content = request.POST.get('news_content', '')
        
        # Preprocess the text
        preprocessed_text = preprocess_text(news_content)
        
        # Load your pretrained model
        model = FakeNewsModel.rfload()  # Load your Random Forest model
        tfidf_v=FakeNewsModel.tfload()
        text_vectorized = tfidf_v.transform([preprocessed_text])
        
        # Make prediction
        prediction = model.predict(text_vectorized)
        if prediction == 0 :
            prediction_label = "Fake News"
        else:
            prediction_label = "Real News"
        # Return prediction as JSON response
        return JsonResponse({'prediction': prediction_label})
    else:
        return JsonResponse({'error': 'Invalid request method'})
