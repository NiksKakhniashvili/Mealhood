from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required
def hungry(request):
    return render(request, "poll/poll1.html", {})