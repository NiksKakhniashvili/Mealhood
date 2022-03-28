from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required




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
        return redirect('poll2')
    
    return render(request, 'poll/poll1.html', {})

@login_required
def reschoose(request):
    if request.method == "POST":
        pass
    
    return render(request, "poll/poll2.html", {})