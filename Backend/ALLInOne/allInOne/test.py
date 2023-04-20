import json
from bs4 import BeautifulSoup 
import requests 
from transformers import pipeline

# Create your views here.

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
def get_text(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    paras = soup.findAll('p')
    text = ''
    for para in paras:
        para = para.get_text()
        text = text + para
        text = get_text(link)
        summary_obj = summarizer(text, max_length=1360, min_length=30, do_sample=False, truncation=True)
        summary = summary_obj[0]['summary_text']
        print(summary)
        return summary
get_text()