from django.forms import ModelForm, widgets
from django.forms import inlineformset_factory


from . import models


class LeadForm(ModelForm):

    class Meta:
        model = models.Lead
        fields = ['id', 'name', 'gender', 'card_number', 'expiry_date', 'professional']
        read_only_fields = ['id']

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ilya Chaban'}),
            'gender': widgets.RadioSelect(),
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXXXXXXXXXXXX'}),
            'expiry_date': widgets.DateInput(attrs={'class': 'datepicker form-control'}),
            'professional': widgets.RadioSelect()
        }


class LanguageForm(ModelForm):
    class Meta:
        model = models.Language
        fields = ['id', 'lead', 'name']
        read_only_fields = ['id']


LanguageFormSet = inlineformset_factory(models.Lead, models.Language,
                                        fields=('name',), extra=1)
