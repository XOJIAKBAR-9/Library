from django import forms

from .models import *


# class TalabaForm(forms.Form):
#     ism = forms.CharField(max_length=250)
#     guruh = forms.IntegerField()
#     kurs = forms.IntegerField(min_value=0, max_value=5)
#     kitob_soni = forms.IntegerField()
#
#
# class MuallifForm(forms.ModelForm):
#     class Meta:
#         model = Muallif
#         fields = "__all__"
#
#
# class Muallifform(forms.ModelForm):
#     class Meta:
#         model = Muallif
#         fields = "__all__"
#
#
# class Recordform(forms.ModelForm):
#     class Meta:
#         model = Records
#         fields = "__all__"

class TalabaForm(forms.Form):
    ism = forms.CharField(max_length=250)
    guruh = forms.CharField(max_length=250)
    kurs = forms.IntegerField(min_value=1, max_value=4)
    kitob_soni = forms.IntegerField(min_value=1, max_value=100000)


class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields="__all__"
