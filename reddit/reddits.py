from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_hot = "https://oauth.reddit.com/r/{subreddit}/hot"
url_wiki_contrib = "https://oauth.reddit.com/r/{subreddit}/about/wikicontributors"
url_mod_list = "https://oauth.reddit.com/r/{subreddit}/about/moderators"

comment_url = "https://oauth.reddit.com/r/{subreddit}/comments/{article}"

class Subreddit(object):

    def __init__(self, subreddit):
        self.subreddit = subreddit

    def hot(self):
        return reddit.client.request(url_hot.format(subreddit=self.subreddit))

    def wiki_contrib(self):
        return reddit.client.request(url_wiki_contrib.format(subreddit=self.subreddit))

    def mod_list (self):

        return reddit.client.request(url_mod_list.format(subreddit=self.subreddit))

class Comments(object):

    def __init__(self, subreddit, article):
        self.subreddit = subreddit
        self.article = article

    def hot(self):
        return reddit.client.request(comment_url.format(subreddit=self.subreddit, article=self.article))

    def search_hot(self, user, subreddit, keyword, fullname, reply):
        info_dic = (Comments(subreddit, fullname).hot()[1]['data']['children'])
        for i in range (0, len(info_dic)):
            if info_dic[i]['data']['body'] == keyword:
                user.comment(info_dic[i]['data']['name'], 'You said: ' + info_dic[i]['data']['body'])
            info_dic += [i]['data']['replies']['data']['children']
            Comments.search_hot(self, user, subreddit, keyword, fullname, reply)
