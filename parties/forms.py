from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Party, Vote


class PartyForm(ModelForm):
    class Meta:
        model = Party
        fields = ['country', 'name', 'acronym', 'leader', 'official_logo', 'description',
                  'website', 'ideologies']
        widgets = {
            'ideologies': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
