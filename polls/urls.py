from django.urls import path
from polls.views import gamodzaxeba,reschoose, volentierman

urlpatterns = [

    path('poll1/', gamodzaxeba, name='poll1'),
    path('poll2/', reschoose, name='poll2'),
    path('poll3/', volentierman, name="poll3")

]