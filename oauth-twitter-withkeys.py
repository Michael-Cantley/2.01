
from requests_oauthlib import OAuth1Session
import secrets
import json
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

client_key = secrets.CONSUMER_KEY
client_secret = secrets.CONSUMER_SECRET

resource_owner_key = secrets.ACCESS_KEY
resource_owner_secret = secrets.ACCESS_SECRET

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
# print (r.text)
#need to print author and text of each tweet!
my_diction = json.loads(r.text)
my_statuses = my_diction["statuses"]
for i in my_statuses:
    my_str = i["text"]
    my_user = i["user"]["screen_name"]
    print(my_str)
    print("-" + my_user)
    print("------------------------------------------------------------------------------")
