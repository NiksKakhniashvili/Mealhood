from django.urls import path
from polls.views import hungry

urlpatterns = [

    path('poll1/', hungry, name='poll1' )

]