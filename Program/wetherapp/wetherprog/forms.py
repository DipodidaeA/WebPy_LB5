from django import forms

class AdminForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20, label="День", required=False)
    d = forms.IntegerField(min_value=1, max_value=31, label="Число", required=False)
    m = forms.IntegerField(min_value=1, max_value=12, label="Місяць", required=False)
    y = forms.IntegerField(min_value=1950, max_value=2024, label="Рік", required=False)
    morn = forms.IntegerField(min_value=-75, max_value=75, label="Зранку", required=False)
    noon = forms.IntegerField(min_value=-75, max_value=75, label="Удень", required=False)
    night = forms.IntegerField(min_value=-75, max_value=75, label="Уночі", required=False)