from django.contrib import admin
from django.urls import path
from eventex.core.views import home
from eventex.subscriptions.views import subscribe

urlpatterns = [
    path('', home),
    path('inscricao/', subscribe),
    path('admin/', admin.site.urls),
]
