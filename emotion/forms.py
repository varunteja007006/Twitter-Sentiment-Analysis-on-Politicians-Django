from django import forms

class emotion_typed_tweet_analyse_form(forms.Form):
    emotion_typed_tweet = forms.CharField(initial='nothing')

class emotion_imported_tweet_analyse_form(forms.Form):
    emotion_imported_tweet = forms.CharField(initial='nothing')