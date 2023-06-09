"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url
from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

# from django.conf.urls import url

from . import views,testdb,search,search2
#
urlpatterns = [
    url(r'^runoob/$', views.runoob),
    url(r'^other/$', views.other),
    url(r'^testdb/$', testdb.testdb),
    url(r'^search_form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search_post/$', search2.search_post),
    url(r'^admin/', admin.site.urls),
]

from django.urls import path

from . import views,testdb

# urlpatterns = [
#     path('', views.),
#     path('/', views.),
#     path('/', ),
#
# ]