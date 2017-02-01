#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

_author = "Eduardo S. Pereira"
_date = "26/05/2016"

import requests


class Apibdtsent:

    def __init__(self, apiID, secretKey,
                 tw_consumer_key=None,
                 tw_consumer_secret=None,
                 tw_access_token=None,
                 tw_access_token_secret=None,
                 localHost=False
                 ):
        self.apiID = apiID
        self.secretKey = secretKey
        self.tw_consumer_key = tw_consumer_key
        self.tw_consumer_secret = tw_consumer_secret
        self.tw_access_token = tw_access_token
        self.tw_access_token_secret = tw_access_token_secret

        if(localHost):
            self.__enderecoApi = 'http://localhost:8000/init/default/api/sent.json'
        else:
            self.__enderecoApi = 'http://api.bigdatatec.com/init/default/api/sent.json'

    def getSentFromText(self, text,
                        listOfNegativeWords=None,
                        listOfPositiveWords=None):
        """
        Rerturn a json with the sentiments associates with a given text and
        its main words .
        key:
            text: list of tweets;
            listOfNegativeWords;
            listOfPositiveWords;
        """

        data = {'apiID': self.apiID,
                'secretKey': self.secretKey,
                'text': text}

        if(listOfNegativeWords is not None):
            data['listOfNegativeWords'] = listOfNegativeWords

        if(listOfPositiveWords is not None):
            data['listOfPositiveWords'] = listOfPositiveWords

        r = requests.post(self.__enderecoApi,
                          params=data)
        return r.json()

    def getSentTweets(self, tweets):
        """
        Rerturn a json with the sentiments associates with each tweet.
        key:
            tweets: list of tweets.
        """
        data = {'apiID': self.apiID,
                'secretKey': self.secretKey,
                'tweets': tweets}

        r = requests.post(self.__enderecoApi,
                          params=data)
        return r.json()

    def sentFromKey(self, keyWord, lat=None, lng=None, raio=None, testMode=0):
        """
        Return a json with the number of positive and negative tweets
        associated with a givem keyWord.
        key:
            keyWord: key word.
        """

        if(lat is not None and lng is not None and raio is not None):
            data = {'apiID': self.apiID,
                    'secretKey': self.secretKey,
                    'keyWord': keyWord,
                    'lat': lat,
                    'lng': lng,
                    'raio': raio,
                    'testMode': testMode
                    }
        else:
            data = {'apiID': self.apiID,
                    'secretKey': self.secretKey,
                    'keyWord': keyWord,
                    'testMode': testMode
                    }
        if(self.tw_consumer_key is not None):
            data['tw_consumer_key'] = self.tw_consumer_key
            data['tw_consumer_secret'] = self.tw_consumer_secret
            data['tw_access_token'] = self.tw_access_token
            data['tw_access_token_secret'] = self.tw_access_token_secret

        r = requests.post(self.__enderecoApi,
                          params=data)
        return r.json()
