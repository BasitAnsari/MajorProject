from django.shortcuts import render
from transformers import pipeline
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@api_view(['POST'])
def summary(request):
    data = request.data
    text = data['text']
    summary_obj = summarizer(text, max_length=1360, min_length=30, do_sample=False, truncation=True)
    summary = summary_obj[0]['summary_text']
    return Response (summary)