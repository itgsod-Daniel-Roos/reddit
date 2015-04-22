from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit
daniel = client.login("playing_blindfolded")

#print daniel.submit('danielsbot', 'self', 'test', 'test_text')

#print client.login('playing_blindfolded').comment('t3_32nyda', 'testcomment')

#print(daniel.karma_per_reddit())

usage_info = Subreddit('danielsbot').hot()['data']['children']

for i in range (0, 24):
    if usage_info[i]['data']['title'] == 'test':
        daniel.comment(usage_info[i]['data']['name'], 'selftext = ' + usage_info[i]['data']['selftext'])

#print (Subreddit('danielsbot').hot()['data']['children'][0]['data']['selftext'])

#python.hot()
