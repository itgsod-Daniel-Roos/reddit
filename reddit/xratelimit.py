from pprint import pprint

import reddit

class Xrate(object):

    def __init__(self):
        pass

    def check(self, response):                              #Checks number of requests left before reset.
        if Xrate().limit(response) < 50:                    #Warning, close.
            return Xrate().warning(Xrate().limit(response), Xrate().time(response))
        else:                                               #General notice.
            return Xrate().notice(Xrate().limit(response), Xrate().time(response))

    def warning(self, requests_remaining, time_remaining):  #Warning text.
        return "Close to limit. {requests} requests remaining. Reset in {time} seconds".format(requests=requests_remaining, time=time_remaining)

    def notice(self, requests_remaining, time_remaining):   #Notice text.
        return "There are {requests} requests remaining. Reset in {time} seconds".format(requests=requests_remaining, time=time_remaining)

    def time(self, response):                               #Returns time left before reset from response.headers.
        return response['x-ratelimit-reset']

    def limit(self, response):                              #Returns requests left before reset from response.headers.
        return response['x-ratelimit-remaining']
