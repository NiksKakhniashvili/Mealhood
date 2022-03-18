from django.contrib import admin
from django.urls import path,include
from members.views import home_page, profile, register, login_user, baseview
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_user, name="login"),
    path('home/', home_page, name='home'),
    path('register/', register, name='register'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'authenticate/logout.html'), name='logout'),
    path('', baseview, name='base'),
    path('profile', profile, name="profile")
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 