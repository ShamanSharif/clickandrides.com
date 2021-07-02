from django import forms


class BookForm(forms.Form):
    pickup = forms.CharField(
        label="Pick-up Point",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    dropOff = forms.CharField(
        label="Drop-off Point",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    viaPoints = forms.CharField(
        label="VIA",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    pickupDateTime = forms.DateTimeField(
        label="Pick-up Date and Time",
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'type': "datetime-local",
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    doBookReturn = forms.BooleanField(
        label="Return",
        widget=forms.CheckboxInput(
            attrs={
                'type': 'checkbox',
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    returnDateTime = forms.DateField(
        label="Return Date and Time",
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                'type': "datetime-local",
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    childSeat = forms.ChoiceField(
        choices=[
            (0, 'Child Seat'),
            (1, '1'),
            (2, '2')
        ],
        label="Child Seat",
        widget=forms.Select(
            attrs={
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
    childBoosterSeat = forms.ChoiceField(
        choices=[
            (0, 'Child Booster Seat'),
            (1, '1'),
            (2, '2')
        ],
        label="Child Booster Seat",
        widget=forms.Select(
            attrs={
                'class': "main-action__book-now__form__text-input"
            }
        )
    )
