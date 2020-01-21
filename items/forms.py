from django import forms
from .models import Category, Item, ProductPhoto, Seller
from django.core.exceptions import ValidationError

''' класс формы соотвествуют полям модели '''


# для переопрделения стилей отображения форм в шаблонах
''' name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your name here',
                'class': 'ask-page-input',
                'label': 'Student Name',
            }
        ))
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Write your Email here',
                'class': 'ask-page-input',
                'label': 'Email',
            }
        ))
    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your Question or Related Subject here',
                'class': 'ask-page-input',
                'label': 'Subject',
            }
        ))

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your message here',
                'class': 'ask-page-input',
                'label': 'Message',
            }
        ))

    source = forms.CharField(  # A hidden input for internal use
        max_length=50,  # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )
 '''



'''    
class CategoryForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(
            attrs={
                'placeholder': 'Write new category',
                'class': 'form-control',
                
            }
        ))
    def clean_title(self): # для валидации полей clean_имя поля 
    	new_cat = self.cleaned_data['title']
    	if Category.objects.filter(title__iexact=new_cat).count():
    		raise ValidationError('Такая категория уже есть')
    	return new_cat

    def save(self):
    	new_category = Category.objects.create(title=self.cleaned_data['title'])
    	return new_category 
'''
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category #прописываем модель 
        fields = ['title']
        
        widgets = {'title' : forms. TextInput(attrs={'placeholder': 'Write new category','class' : 'form-control'})}
        
        def clean_title(self): 
        	new_cat = self.cleaned_data['title']
        	if Category.objects.filter(title__iexact=new_cat).count():
        		raise ValidationError('Такая категория уже есть')
        	return new_cat
        

class ItemForm(forms.Form):
	pass
