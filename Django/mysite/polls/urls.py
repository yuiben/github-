"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    #đặt tên path bằng name sẽ truy vấn dễ dàng ở template vidu ở questionList.html dòng 16
    path('detail/<int:question_id>/', views.detailView, name = 'view_detail'),
    path('list/',views.viewlist, name = 'view_list'),
    path('', views.index, name="index"),
    path('viewchoice/',views.vote, name='vote')
]
