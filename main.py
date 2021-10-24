import requests
import json
url = 'https://www.mindphp.com/'
r = (requests.get(url))

print(r.content)
print(r.encoding)
print(r.text)
url_file = 'https://www.mindphp.com/images/info/mindphp.png'
chue_file = 'mindphp.jpg'
r= requests.get(url_file)
with open(chue_file,'wb') as f:
    f.write(r.content)
r = requests.get('https://hinaboshi.com')
with open('hinaboshi.html','wb') as f:
    f.write(r.content)
url_file = 'https://hinaboshi.com/rup/rupprakopwalidet/1460321927319907.jpg'
chue_file = 'tapris.jpg'
r = requests.get(url_file)
with open(chue_file,'wb') as f:
    f.write(r.content)