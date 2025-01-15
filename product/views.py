from django.shortcuts import render,  get_object_or_404, redirect
from .forms import ProductForm, SearchForm
from .models import Product
from math import ceil 
from django.db.models import Q
from .pagination import pagination

# def index(request):
# 	products  = Product.objects.all()
# 	print(products)
# 	n = len(products)
# 	nslides  = n//4 +ceil((n/4)-(n//4))
# 	params = {'no_of_slides':nSlides, 'range':range(nSlides), 'product':products}
# 	return render (request, "product/product_list.html", params)


def product_view(request):
	queryset = Product.objects.all() 	#list of objects
	pages = pagination(request,queryset,5)
	context = {
		"items" : pages[0],
		'page_range': pages[1]

	}
	return render (request, "product/product_list.html", context)
 

def product_create_view(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		new_obj = form.save(commit=False)
		#new_obj.created_by = request.user
		new_obj.save()
		form = ProductForm()
	context = {
		'form' : form 
   
	}

	return render (request, "product/product_create.html", context)


def dynamic_lookup_view(request,my_id):
	# obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product, id=my_id)
	context = {
		"object":obj
	}
	return render (request, "product/product_detail.html", context)

def contact_view(request):
	return render(request, "product/contact.html")


# def Filter_view(request):
# 	search_query = SearchForm(request.GET or None)
# 	qs = Product.objects.all() 
# 	title_contains =request.GET.get('title')

# 	if title_contains != "" and title_contains is not None:
# 		qs = qs.filter(title__icontains=title_contains)

# 	context= {
# 	'queryset':qs
# 	}
	

# 	return render (request, "product/product_list.html", context)


# def Filter_view(request):
# 	queryset = Product.objects.all()
# 	allProds = []
# 	catprods = Product.objects.values('category','id')
# 	cats = {item['category'] for item in catprods}
# 	for cat in cats:
# 		prod = Product.objects.filter(category=cat)
# 		n = len(prod)
# 		allProds.append([prod])
# 	context = {'object_list':allProds}
# 	return render (request, "product/product_list.html", context)


def search(request):
	template = 'product/product_list.html'
	query = request.GET.get('q')
	if query:
		results = Product.objects.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(sub_category__icontains=query))
	else:
		results = Product.objects.all()

	pages = pagination(request, results, num =10)
	context={
		'items':pages[0],
		'page_range': pages[1]
	}

	return render(request, 'product/product_list.html', context)
 



