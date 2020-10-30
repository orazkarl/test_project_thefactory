from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('set_telegram_user_id/', views.set_telegram_user_id, name='set_telegram_user_id'),
    path('send_message/', views.send_message, name='send_message'),

]
