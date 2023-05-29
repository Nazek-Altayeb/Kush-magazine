"""magazine URL Configuration

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
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_article, name='add'),
    path('', views.get_article, name='get_article'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('get_topic/', views.get_topic, name='get_topic'),
    path('edit/<article_id>', views.edit_article, name='edit_article'),
    path('delete/<article_id>', views.delete_article, name='delete_article')
]
