from django import forms


class AddProduct(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    pic = forms.CharField(max_length=300)


