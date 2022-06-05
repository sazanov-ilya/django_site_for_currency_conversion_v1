from django.urls import path
from exchange_app.views import exchange

urlpatterns = [
    path('', exchange),
]