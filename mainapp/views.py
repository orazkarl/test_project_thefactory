from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
import telebot

TELEGRAM_BOT_TOKEN = '1088972154:AAH10CkfPAvkK22dJxx-ILrl-qUvtY6LRDo'


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class IndexView(generic.TemplateView):
    template_name = 'index.html'

@login_required(login_url="/accounts/login")
def set_telegram_user_id(request):
    if request.POST:
        user = request.user
        telegram_user_id = request.POST['telegram_user_id']
        user.telegram_user_id = telegram_user_id
        user.save()
        return redirect('/')

@login_required(login_url="/accounts/login")
def send_message(request):
    if request.POST:
        user = request.user
        message = request.POST['message']
        url = 'http://localhost:8000/api/message/create'
        response = requests.post(url, data={'user': user.id, 'message': message})
        if response.status_code == 201:
            bot = telebot.TeleBot('1088972154:AAH10CkfPAvkK22dJxx-ILrl-qUvtY6LRDo')
            msg = f'{user.username}, я получил от тебя сообщение ' + '\n' + message
            bot.send_message(user.telegram_user_id, text=msg)

    return redirect('/')
