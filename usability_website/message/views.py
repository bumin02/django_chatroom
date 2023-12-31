from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model


from .models import Chat, Message

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

    print("hello?")
    for chat in chats:
        print(type(chat))
        print("chat name: ", chat.name)
        print("chat slug: ", chat.slug)
    print("where is that")

    # return render(request, 'message/message.html', {'users': users, 'chat': chat, 'chat_history': chat_history})
    return render(request, 'message/messages.html', {'users': users, 'chats': chats})

@login_required
def message(request, slug):

    user = get_user_model()
    users = user.objects.all()

    chat = Chat.objects.get(slug=slug)
    chat_history = Message.objects.filter(chat=chat).order_by('-date_added')[0:25][::-1]
    friends = Chat.objects.all()

    for i in users:
        print(type(i))
        print(i == request.user.username)

    print(type(request.user.username))
    print(request.user.username)

    # return render(request, 'message/message.html', {'chat': chat, 'chat_history': chat_history})
    return render(request, 'message/message.html', {'users': users, 'friends': friends, 'chat': chat, 'chat_history': chat_history})