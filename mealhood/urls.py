from django.contrib import admin
from django.urls import path,include
from members.views import home_page, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('home/', home_page, name='home'),
    path('register/', register, name='register'),

]
 