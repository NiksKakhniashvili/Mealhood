from django.urls import path
from polls.views import gamodzaxeba,reschoose

urlpatterns = [

    path('poll1/', gamodzaxeba, name='poll1'),
    path('poll3/', reschoose, name='poll2')

]