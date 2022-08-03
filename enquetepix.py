from os import read, write
import tweepy
import time
import random

# Load keys (Carregar suas chaves)
api_key = 'your api key'
api_secret_key = 'your secret key'
acess_key = 'your access key'
acess_secret = 'your secret access'
bearer_token = 'Your bearer token'

#Load api client(Carrega a api do twitter client)
def getClient():
    client = tweepy.Client(bearer_token,
                    api_key,
                    api_secret_key,
                    acess_key,
                    acess_secret)
    return client

#Search tweets(Funcao para procurar tweet passando as chaves e a query)
def searchTweets(client, query):
    # search recent tweets com no maximo 30 resultados (colocar até 100)
    tweets = client.search_recent_tweets(query=query, max_results=30)
    #Record data on tweet_data(grava os dados na variavel tweet_data)
    tweet_data = tweets.data 
    
    results = []
    # If have found(se achou algum tweet)
    if not tweet_data is None and len(tweet_data) > 0:
        #percorre os dados do Tweet_data
        for tweet in tweet_data:
          #Record the results on obj array(grava os resultados em um array chamado obj)
          obj = {}
          obj['id'] = tweet.id
          obj['text'] = tweet.text
          results.append(obj)
    
    return results

#
"""
def getTweet(client, id):
    tweet = client.get_tweet(id, expansions=['author_id'], user_fields=['username'])
    return tweet
"""
#Load api(carrega a api)
client = getClient()
#Call the function search tweets(chama a função para procurar tweets com a string que deve procurar) 
tweets = searchTweets(client,'em quem votar')
#var with the answer(variavel com a resposta dos tweets achados)
tuitar = "Alguém realmente confia nessas pesquisas eleitorais? Entre nesse site, cadastre mostre sua intenção de voto e escreva o motivo, é um site de enquete que mostra realmente qual candidato esta na frente. https://enquetepix.com.br curtam e compartilhem"
objs = []

if len(tweets) > 0: 
    for tweet in tweets:
   #     twt = getTweet(client, tweet['id'])
        #Reply a tweety found with words from var tuitar(responder o twitter encontrado com a palavra da variavel tuitar)
        client.create_tweet(in_reply_to_tweet_id=tweet['id'], text= tuitar)
        #Print tweet id and text(printar o id e o texto do twitter achado)
        print(str(tweet['id'])+" escreveu" + str(tweet['text']))
        
 



