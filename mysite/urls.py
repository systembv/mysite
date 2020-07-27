from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('polls/', include('polls.urls')),
    path('', include('tasks.urls')),
    #path('users/', include('users.urls')),
    #path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]