from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Policy, Vote


class PolicyForm(ModelForm):
    class Meta:
        model = Policy
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PolicyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['value', 'comment']

        labels = {
            'name': 'Place your vote',
            'comment': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
