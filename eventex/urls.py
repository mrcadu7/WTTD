from django.contrib import admin
from django.urls import path
from eventex.core.views import home
from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    path('', home),
    path('inscricao/', subscribe),
    path('inscricao/<int:pk>/', detail),
    path('admin/', admin.site.urls),
]
