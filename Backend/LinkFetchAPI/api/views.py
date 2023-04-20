import json
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from googlesearch import search

# Create your views here.
def get_links(query, domains, count):
  query = f'criminal news in {query} site:indianexpress.com'
  links = []
  for j in search(query, tld="co.in", tbs= "qdr:d" ,num=count, stop=count, pause=5):
    links.append(j)
  return links


@api_view(['POST'])
def linkFetch(request):
    data = request.data
    print(data)
    query = data["query"]
    count = 10
    domains = [
    "indianexpress.com",
    ]
    links = {"links" : get_links(query, domains,count)}
    res = json.dumps(links)
    return Response (res)
    