"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]

from qa.views import test, news, popular, question, ask
from login.views import signup, LogIn

urlpatterns = [
    url(r'^$',news),
    url(r'login/', LogIn),
    url(r'signup/',signup),
    url(r'question/(?P<_id>\d+)/', question),
    url(r'ask/',ask),
    url(r'popular/', popular),
    url(r'new/', test),
]
