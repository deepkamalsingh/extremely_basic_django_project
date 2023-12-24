"""
To render html web pages
"""

from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string



def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    article_queryset = Article.objects.all()
    context = {
        "article_list": article_queryset,
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING)