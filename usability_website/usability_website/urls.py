from django.contrib import admin
from django.urls import path, include
from room import views

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('profile/', include('profilestatus.urls')),
    path('admin/', admin.site.urls),
    path('message/', include('message.urls')),

]
