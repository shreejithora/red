from django import forms 
from .models import DateCategoryModel, DonateModel

class DonateForm(forms.ModelForm):
    class Meta:
        model = DonateModel
        fields = '__all__'
    # name = forms.CharField(label='name', max_length=255)
    # contact = forms.CharField(label='contact', max_length=120)
    # address = forms.CharField(label='address', max_length=255)
    # datecategory = forms.ForeignKey(DateCategoryModel,on_delete=models.CASCADE)
    # timestamp = froms.DateTimeField(auto_now_add=True)