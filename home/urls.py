from django.urls import path, re_path
from .views import login_view, logout_view, register_view, home_view, event_view, profile_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('event/', event_view, name='event'),
    path('profile/', profile_view, name='profile'),
    path('', home_view, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
