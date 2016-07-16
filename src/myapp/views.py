from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404


from .forms import CompraModelForm
from .models import ComprarArticulo

#Create your views here.
