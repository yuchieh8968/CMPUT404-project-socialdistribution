from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Create your views here.
def react(request):
    if not request.user.is_active:
        return redirect(reverse_lazy('login'))
    else:
        return render(request, "index.html")