from django.shortcuts import render

from django.http import HttpResponse
from apps.materials.forms import *
from django.http import HttpResponseRedirect
import json
from django.core import serializers

def index(request):
    context = {}
    return render(request, 'trucks/index.html', context)

def materials(request):
	if request.method == 'POST':
		form = MaterialsForm(request.POST)
		if form.is_valid() and request.user.is_staff:
			materials = form.save(commit=False)
			materials.created_by = request.user
			materials.save()
			return HttpResponseRedirect('/')
	else:
		form = MaterialsForm()
	return render(request, 'materials/materials_main.html', {'form':form})

from django.http import JsonResponse
def materials_list(request):
	materials_list = Materials.objects.all()
	serialized_obj = serializers.serialize('json', materials_list)
	print serialized_obj
	return JsonResponse(json.loads(serialized_obj), safe=False)