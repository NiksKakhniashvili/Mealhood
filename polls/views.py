import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Poll



# @login_required
# def gshia(request):
#     if request.method == 'POST':
#         if request.POST.get("action") == 'yes':
#             return redirect('poll2')    
#         else:
#             return redirect('home')
#     return render(request, "poll/poll1.html", {})

@login_required
def gamodzaxeba(request):
    if request.method == 'POST':
        if Poll.objects.filter(user=request.user).exists():
            Poll.objects.get(user=request.user).delete()

        if request.POST.get("action") == 'yes':
            Poll.objects.create(garet=True, user=request.user)
        else:
            Poll.objects.create(garet=False, user=request.user) 
        return redirect('poll2')
    
    return render(request, 'poll/poll1.html', {})


@login_required
def reschoose(request):
    food = Food.objects.all()
    context = {
        'food': food
    }

    if request.method == "POST":
        request_data = request.POST.get('restaurant_name')
        if request_data == 'გახსენით მენიუ':
            context['error'] = 'გთხოვთ აირჩიოთ რესტორანი ბლიად'
            return render(request, "poll/poll2.html", context)
        food = Food.objects.get(foods=request_data)
        Poll.objects.update(user=request.user, essen=food)
        return redirect("poll3")

    return render(request, "poll/poll2.html", context)


def volentierman(request):
    if request.method == "POST":
        if request.POST.get("action") == "yes":
            Poll.objects.update(user=request.user,volentier=True)
    return render(request, "poll/poll3.html",{})