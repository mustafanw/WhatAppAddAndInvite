import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.whatsappgroupsjoinlink.com/loot-deals-and-tricks-whatsapp-group-links/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    if 'chat.whatsapp.com' in link:
        print(link.get('href'))