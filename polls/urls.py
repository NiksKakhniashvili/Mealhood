from django.urls import path
from polls.views import gshia,gamodzaxeba

urlpatterns = [

    path('poll1/', gshia, name='poll1'),
    path('poll2/', gamodzaxeba, name='poll2'),
#    path('poll3/' reschoose, name='poll3')

]