from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_about = "https://oauth.reddit.com/api/v1/user/{username}/about"
url_karma = "https://oauth.reddit.com/api/v1/me/karma"
url_submit = "https://oauth.reddit.com/api/submit"
url_comment = "https://oauth.reddit.com/api/comment"

class User(object):

    def __init__(self, reddit_id):
        self.id = reddit_id


    def me (self):

        return reddit.client.request(url_me)

    def link_karma (self):

        return reddit.client.request(url_me)['link_karma']

    def karma_per_reddit (self):

        return reddit.client.request(url_karma)

    def submit(self, subreddit, kind, title, text):

        data = {'sr': subreddit, 'kind': kind, 'title': title, 'text': text}

        return reddit.client.request_data(url_submit, data)

    def comment(self, id, text):

        data = {'thing_id': id, 'text': text}

        return reddit.client.request_data(url_comment, data)
