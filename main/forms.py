from django import forms

class BookForm(forms.Form):
	pickup = forms.CharField(label="Pick-up Point", max_length=255, widget=forms.TextInput(attrs={'class': "main-action__book-now__form__text-input"}))
	dropoff = forms.CharField(label="Drop-off Point", max_length=255, widget=forms.TextInput(attrs={'class': "main-action__book-now__form__text-input"}))
