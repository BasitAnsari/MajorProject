from django.shortcuts import render
import json
from bs4 import BeautifulSoup 
import requests 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

links = ["https://indianexpress.com/article/cities/mumbai/bank-employee-held-for-duping-man-of-rs-6-8l-over-1600-salary-accounts-under-scrutiny-8538674/"]


def get_text(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    paras = soup.findAll('p')
    text = ''
    for para in paras:
      para = para.get_text()
      text = text + para
    return text

@api_view(['POST'])
def getText(request):
    data = request.data
    link = data["link"]
    text = get_text(link)
    res = json.dumps(text)
    return Response (res)