from django import forms

class AnswerForm(forms.Form):
    target = forms.CharField(widget=forms.HiddenInput(), initial='')
    infinitive = forms.CharField(label='Infinitive', max_length=100)
    past_simple = forms.CharField(label='Past simple', max_length=100)
    past_participle = forms.CharField(label='Past participle', max_length=100)
    