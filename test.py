from twarc import Twarc

client_key = 'qkyfU7RwPyDAvcn7KpdVeLvGC'
client_secret = 'ng3MiWHh2pfRERdCgR2Ob0zRzrMi06LKgcY42SgXPPuyiBvu2p'
access_token = '197456523-m2qIYWxkQTFKj0ModTQPcdByTnjryHwLRm9L8o5y'
access_token_secret = 'sTT7MqYIOWPZHEZiub8ppTQUCPNIxnjkMaAiAxa0126rp'

t = Twarc(client_key, client_secret, access_token, access_token_secret)
for tweet in t.search("resigncameron"):
    print(tweet["text"])
