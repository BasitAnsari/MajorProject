import json
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from googlesearch import search
from django.core.cache import cache
# Create your views here.
def get_links(query, domains, count):
  query = f'criminal news in {query} site:indianexpress.com'
  links = []
  for j in search(query,num=count, start=10, stop=count, pause=5):
    links.append(j)
  return links


@api_view(['POST'])
def linkFetch(request):
    data = request.data
    query = data["query"]
    count = 10
    domains = [
    "indianexpress.com",
    ]
    links = get_links(query, domains,count)
    f = open('media/data.json')
    cache = json.loads(f.read())
    cacheSum = []
    for link in links:
      cachedData = cache.get(link)
      print (cachedData)
      if cachedData:
        cacheSum.append([link,cachedData])
        links.pop(links.index(link))
    links = {"links" : links, 'cacheSum':cacheSum}
    print(links)
    res = json.dumps(links)
    return Response(res)