from django import forms

class SurveyForm(forms.Form):
        title = forms.CharField()
        question = forms.CharField()
        answer = forms.CharField()
