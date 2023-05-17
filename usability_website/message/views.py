from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model


from .models import Student

@login_required
def message(request):
    
    user = get_user_model()
    users = user.objects.all()
    # users = Student.objects.filter(pk=1).values_list('Username', flat=True)
    # print(type(users))

    # get own username, dont make an entry for own username!

    # for i in users:
    #     print(i.username)
    return render(request, 'message/message.html', {'users': users})
