from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from profilestatus.forms import EditProfileForm
# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()

            print("saved.")

    else:
        form = EditProfileForm()


    form = EditProfileForm(instance=request.user)
    args = {'form': form}     
    return render(request, 'profilestatus/profile.html', args)
