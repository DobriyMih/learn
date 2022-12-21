from django.shortcuts import render
from django.http import HttpResponse
from  .forms import UserForm
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привіт, {name}, твій вік: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form":userform})