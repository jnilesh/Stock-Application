from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

def home(request):
	return render(request,'home.html',{})

def list(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker + "/quote?token=pk_ea80f000f706407abed481edb1ae1f8c")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"
		return render(request,'list.html',{'api':api})	

	else:
		return render(request,'list.html',{'ticker':'Enter a ticker above'})
		

	

def about(request):
	return render(request,'about.html',{})


def add_stock(request):
	if request.method == 'POST':
		form = StockForm(request.POSt or None)

		if form.is_valid():
			form.save()
			messages.sucess(request,("Stock has been Added"))
			return redirect('add_stock')


	ticker = Stock.objects.all()
	return render(request,'add_stock.html',{'ticker':ticker})	


def delete_ticker(request,stock_id):
	item = Stock.object.get(pk=stock_id)
	item.delete()
	messages.success(request,("Stock has been deleted!"))
	return redirect('add_stock')
