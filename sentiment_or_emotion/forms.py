from django import forms

class Sentiment_Imported_Tweet_analyse_form(forms.Form):
    sentiment_imported_tweet = forms.CharField(initial='nothing')