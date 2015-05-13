from pprint import pprint

import reddit

class Xrate(object):

    def __init__(self):
        pass

    def check(self, response):
        if Xrate().limit(response) < 50:
            return Xrate().warning(Xrate().limit(response), Xrate().time(response))
        else:
            return Xrate().notice(Xrate().limit(response), Xrate().time(response))

    def warning(self, requests_remaining, time_remaining):
        return "Close to limit. {requests} requests remaining. Reset in {time} seconds".format(requests=requests_remaining, time=time_remaining)

    def notice(self, requests_remaining, time_remaining):
        return "There are {requests} requests remaining. Reset in {time} seconds".format(requests=requests_remaining, time=time_remaining)


    def time(self, response):
        return response['x-ratelimit-reset']

    def limit(self, response):
        return response['x-ratelimit-remaining']
