from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model


from .models import Chat#, Message

@login_required
# def message(request, slug):
def messages(request):

    user = get_user_model()
    users = user.objects.all()

    for i in users:
        print(type(i))
        print(i.username)

    chats = Chat.objects.all()
    # chat_history = Chat.objects.filter(chat=chat).order_by('-date_added')[0:25][::-1]

    for chat in chats:
        print(type(chat))
        print("chat name: ", chat.name)
        print("chat slug: ", chat.slug)

    # return render(request, 'message/message.html', {'users': users, 'chat': chat, 'chat_history': chat_history})
    return render(request, 'message/messages.html', {'users': users, 'chats': chats})

@login_required
def message(request, slug):
    chat = Chat.objects.get(slug=slug)
    # chat_history = Message.objects.filter(chat=chat).order_by('-date_added')[0:25][::-1]

    # return render(request, 'message/message.html', {'chat': chat, 'chat_history': chat_history})
    return render(request, 'message/message.html', {'chat': chat})