from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Neighborhood,Profile,Business,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm, NewBusinessForm, NewPostForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
  neighborhoods = Neighborhood.get_all_neighborhoods()
  return render(request, 'index.html',{"neighborhoods":neighborhoods})

