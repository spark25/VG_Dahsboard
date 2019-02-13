from django import forms



class DateFilterForm(forms.Form):
    from_date = forms.DateField(label="", widget=forms.TextInput(attrs={'placeholder': 'From'}))
    to_date = forms.DateField(label="", widget=forms.TextInput(attrs={'placeholder': 'To'}))