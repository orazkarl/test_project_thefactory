from django.urls import path, include
from . import views
urlpatterns = [
    path('message/create', views.MessageCreateView.as_view(), name='message_create')
]
