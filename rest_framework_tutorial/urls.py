from django.contrib import admin
from django.urls import path, include                                       #add o include para pode jogar para outro arquivo url.py do projeto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escola/',include('escola.urls'))                                 #jogando a url relativa 'escola/' para a pasta escola dentro desse projeto
]
