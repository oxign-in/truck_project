from django.shortcuts import render

from django.http import HttpResponse
from apps.goods.forms import *
from django.http import HttpResponseRedirect

def index(request):
    context = {}
    return render(request, 'trucks/index.html', context)

def goods(request):
	if request.method == 'POST':
		form = GoodsForm(request.POST)
		if form.is_valid() and request.user.is_staff:
			goods = form.save(commit=False)
			goods.created_by = request.user
			goods.save()
			return HttpResponseRedirect('/')
	else:
		form = GoodsForm()
	return render(request, 'goods/goods_main.html', {'form':form})

def goods_list(request):
	goods_list = Goods.objects.all()
	return render(request, 'goods/list.html', {'goods_list':goods_list})