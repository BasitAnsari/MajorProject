from django.shortcuts import render
import json
from bs4 import BeautifulSoup 
import requests 
# from transformers import pipeline
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
def get_text(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    paras = soup.findAll('p')
    text = ''
    for para in paras:
      para = para.get_text()
      text = text + para
    return text
def query(payload):
  API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
  headers = {"Authorization": "Bearer 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"}
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()
@api_view(['POST'])
def summary(request):
    data = request.data
    link = data["link"]
    text = get_text(link)
    summary = query({
	"inputs": text,
    }) 
    return Response (summary[0])