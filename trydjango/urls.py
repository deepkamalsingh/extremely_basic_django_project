"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view
from articles import views as article_views
from accounts import views as accounts_views

urlpatterns = [
    path('', home_view),
    path('articles/',article_views.article_search_view),
    path('articles/create/',article_views.article_create_view),
    path('articles/<int:id>/',article_views.article_detail_view),
    path('admin/', admin.site.urls),
    path('login/',accounts_views.login_view),
    path('logout/',accounts_views.logout_view),
    path('register/',accounts_views.register_view),
]
