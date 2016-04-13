from twarc import Twarc

client_key = 'client_key'
client_secret = 'client_secret'
access_token = '197456523-m2qIYWxkQTFKj0ModTQPcdByTnjryHwLRm9L8o5y'
access_token_secret = 'access_token_secret'

t = Twarc(client_key, client_secret, access_token, access_token_secret)
for tweet in t.search("resigncameron"):
    print(tweet["text"])
