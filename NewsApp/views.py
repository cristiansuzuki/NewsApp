from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

# Função que faz requisição da API de acordo com os paramêtros passados


def index(request):
    newsApi = NewsApiClient(api_key='17af1b67e52a44fa85a60b1f052df07d')

    # Abaixo está o parametro get_top_headlines. Para pegar todos os dados de uma palavra
    # pode-se usar get_everything e passar 'q=nomedapalavra' dentro da função

    headLines = newsApi.get_top_headlines(sources="bleacher-report")
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist = zip(news, desc, img, url)

    return render(request, "index.html", context={"mylist": mylist})
