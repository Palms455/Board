from django import forms
from .models import Category, Item, ProductPhoto, Seller
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from django.forms import modelformset_factory, inlineformset_factory
from django.forms import BaseInlineFormSet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



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
        

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, to_field_name="title")
        seller =forms.ModelChoiceField(queryset=Seller.objects.all(), empty_label=None, to_field_name="title")
        fields = ['title', 'description', 'seller', 'price', 'category', 'adress' ]
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'Название','class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'placeholder': 'Описание','class' : 'form-control'}),
            
            'price' : forms.NumberInput(attrs={'placeholder': 'Стоимость','class' : 'form-control'}),
           
            'adress' : forms. TextInput(attrs={'placeholder': 'Адрес','class' : 'form-control'})
            }



class PhotoForm(forms.ModelForm):
    #photo = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'})) # усли надо выбрать много файлов

    photo = forms.ImageField(label='Image') 
    class Meta:
        model = ProductPhoto
        fields = ['photo']

PhotoFormSet = modelformset_factory(ProductPhoto,form=PhotoForm, can_delete=True, extra=3)
PhotoInlineFormSet = inlineformset_factory(Item, ProductPhoto, fields=('photo',), form=PhotoForm,  max_num=3)
        #def save(self, id):
        #    new_photo = ProductPhoto.objects.create(photo=self.cleaned_data['photo'], product = id)
        #    return new_photo  
    

 # https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django

class AuthUserForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ('username', 'password')
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Имя пользователя','class' : 'form-control mb-2'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль','class' : 'form-control mb-2-2'}),
            }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuthUserForm, self).__init__(*args, **kwargs)

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('username', 'password','email' ,'first_name', 'last_name')
       
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Имя пользователя','class' : 'form-control mb-2'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль','class' : 'form-control mb-2-2'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Имя пользователя','class' : 'form-control mb-2'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Пароль','class' : 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Пароль','class' : 'form-control mb-2'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

        