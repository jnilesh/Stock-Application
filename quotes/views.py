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
	import requests
	import json

	api_request = requests.get("https://cloud.iexapis.com/beta/ref-data/symbols?token=pk_ea80f000f706407abed481edb1ae1f8c")
	try:
		api = json.loads(api_request.content)			
	except Exception as e:
		api = "Error"
	return render(request,'about.html',{'api':api})


def add_stock(request):
	import requests
	import json


	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			var = request.POST.get("ticker")
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(var) + "/quote?token=pk_ea80f000f706407abed481edb1ae1f8c")

			try:
				api = json.loads(api_request.content)			
			except Exception as e:
				api = "Error"
				messages.error(request,("Error in ticker name!"))
				return redirect('add_stock')

			form.save()
			messages.success(request,("Stock has been Added"))
			return redirect('add_stock')

	else:
	
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) + "/quote?token=pk_ea80f000f706407abed481edb1ae1f8c")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error"

	return render(request,'add_stock.html',{'output':output})	


def delete_ticker(request,symbol):
	item = Stock.objects.get(pk=symbol.lower())
	item.delete()
	messages.success(request,("Stock has been deleted!"))
	return redirect('add_stock')


def detail_view(request,symbol):
	import requests
	import json

	if symbol:

		api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ symbol + "/quote?token=pk_ea80f000f706407abed481edb1ae1f8c")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"
		return render(request,'detail_view.html',{'api':api})	

	else:
		return render(request,'list.html',{'ticker':'You Shoul Not Be Here!'})