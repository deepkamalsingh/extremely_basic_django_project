from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

def article_search_view(request):
    # print("my name is ")
    # print(request.GET)
    query_dict = request.GET
    query = query_dict.get("q")
    try:
        query = int(query)
    except:
        query = None 
    obj = None 
    if query:
        obj = Article.objects.get(id=query)
    context = {
        "obj": obj
    }
    # print(dir(request))
    return render(request, "articles/search.html", context=context)

def article_detail_view(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "obj" : article_obj
    }
    print(article_obj)
    return render(request,'articles/detail.html',context=context)

# @csrf_exempt
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {"form" : form}
    if form.is_valid():
        obj = form.save()
        context["form"] = ArticleForm()
    return render(request,'articles/create.html',context=context)