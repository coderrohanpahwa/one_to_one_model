from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import AnswerForm
k="Annonymous User"
def index(request):
    fm=AnswerForm()
    return render(request,'course/index.html',{'form':fm})
