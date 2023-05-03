from django import forms
from .models import Ads,Responses



class AdsForm(forms.ModelForm):
    title = forms.CharField(max_length=34)
    class Meta:
        model = Ads
        fields = ['title','content','category',]
        exclude =['dateCreation']


class ResponseForm(forms.ModelForm):
    comment=forms.CharField(label='Комментарий')
    class Meta:
        model = Responses
        fields = [
            'comment',
        ]










