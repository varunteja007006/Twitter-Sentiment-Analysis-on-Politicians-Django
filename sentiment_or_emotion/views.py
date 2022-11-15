from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, TemplateView

from .sentiment_analysis_code import sentiment_analysis_code
from .forms import Sentiment_Imported_Tweet_analyse_form

from .tweepy_sentiment import import_tweet_sentiment


def choose_sentiment_or_emotion(request):
    return render(request, 'home/home.html')

def trending(request):
    if request.method == 'POST':
        form = Sentiment_Imported_Tweet_analyse_form(request.POST)
        tweet_text = import_tweet_sentiment()
        analyse = sentiment_analysis_code()

        if form.is_valid():
            handle = form.cleaned_data['sentiment_imported_tweet']

            if handle[0]=='#':
                list_of_tweets = tweet_text.get_hashtag(handle)
                list_of_tweets_and_sentiments = []
                for i in list_of_tweets:
                    list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment(i)))
                args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
                return render(request, 'home/trending_result_hashtag.html', args)

            list_of_tweets = tweet_text.get_tweets(handle)
            
            list_of_tweets_and_sentiments = []
            

            for i_tweet,i_likes,i_retweet,i_tweeted_at in list_of_tweets:
                list_of_tweets_and_sentiments.append((i_tweet,analyse.get_tweet_sentiment(i_tweet),i_likes,i_retweet,i_tweeted_at))


            if handle[0]!='@':
                handle = str('@'+handle)    

            args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle, }
            return render(request, 'home/trending_result.html', args)

    else:
        
        return render(request, 'home/Trending.html')