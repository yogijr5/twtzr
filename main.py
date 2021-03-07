#Import Librari
from textblob import TextBlob
import tweepy
import sys


#API & Secret Key
mykeys = open('api.txt', 'r').read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

#Input Topik Dan Jumlah Tweet
print("\n")
print(f'Mesin Penilai Sentimen Topik Twitter. dibuat oleh: @_yogijr')
print(f'Note: Jumlah tweet yang dimasukkan akan berpengaruh dalam menilai sentimen' 
"\n nilai ideal adalah : 200")
print("\n")
search_term = input('Masukkan Topik Pencarian : ')
tweet_amount = int(input('Masukkan Jumlah Tweet : '))

tweets = tweepy.Cursor(api.search, q=search_term, lang='id').items(tweet_amount)

#Polarity Dan Sentimen
polarity = 0


positive = 0 
neutral = 0
negative = 0

#Proses Logic Sentimen, Polarity dan Final
for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
        negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += analysis.polarity
    print(final_text)
    



#Penampilan / Print Text
print("\n")
print(f'Topik Tweet: {search_term}')
print(f'Nilai Polarity : {polarity}')
print(f'Jumlah Tweet Positif: {positive}')
print(f'Jumlah Tweet Negatif: {negative}')
print(f'Jumlah Tweet Netral: {neutral}')