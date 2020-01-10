import requests
import webbrowser
param = {"wd":"莫烦Python","wd":"马泽伟","wd":"fuck"}
r = requests.get('http://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)
data = {'firstname':'mazewei','lastname':'father'}
n = requests.post('http://pythonscraping.com/pages/files/processing.php',data=data)
print(n.text)




payload = {'username': 'Morvan', 'password': 'password'}
q = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(q.cookies.get_dict())
# {'username': 'Morvan', 'loggedin': '1'}
x = requests.get('http://pythonscraping.com/pages/cookies/welcome.php', cookies=q.cookies)
print(x.text)
# Hey Morvan! Looks like you're still logged into the site!
