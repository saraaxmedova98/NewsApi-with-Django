from django.shortcuts import render
from newsapi import NewsApiClient
import random
from datetime import datetime 
# Create your views here.

def news_detail(request):
    newsapi = NewsApiClient(api_key='dad92c4713cc4022bac995b6b6456d95')

    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')
    
    articles = top_headlines['articles']
    titles = []
    description = []
    images = []
    publishing_date = []
    author = []
    for index in range(len(articles)):
        articles_list = articles[index]
        
        titles.append(articles_list['title'])
        description.append(articles_list['description'])
        images.append(articles_list['urlToImage'])
        publishing_date.append(articles_list['publishedAt'])
        author.append(articles_list['author'])
    
    news_list = zip(titles, description, images, publishing_date, author)
    context = {"news_list" : news_list}
    return render( request , 'news.html', context)
    