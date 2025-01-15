from django import forms
from .models import Product
 

class ProductForm(forms.ModelForm): 
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title "})								)
	description = forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder":"Your description"}))
	age = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"How old is your product"}))
	#image 		= forms.ImageField(upload_to ="product/images", null=True)

	image = forms.ImageField(required=False)

	class Meta:
		model = Product 
		fields = [
			'image',
			'title',
			'summary',
			'description',
			'price',
			'category',
			'sub_category',
			'age'

		]


class SearchForm(forms.ModelForm):
	search = forms.CharField(label='', widget=forms.TextInput(attrs ={"placeholder":"search"}))

	# def clean_image(self, *args,**kwargs):
	# 	image = self.cleaned_data.get("image")
	# 	 #### if not can be used if need multiple validation types


	# def clean_size(self, *args,**kwargs):
	# 	size = self.cleaned_data.get("title")
	# 	if 'CFE' in title:
	# 		return title
	# 	else:

	# 		raise forms.ValidationError("This is not a valid title") #### if not can be used if need multiple validation types

	# 		raise forms.ValidationError("This is not a valid title") #### if not can be used if need multiple validation types

