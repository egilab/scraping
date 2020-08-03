import requests
import bs4

all_articel = []
url = 'https://www.detik.com/terpopuler'
get = requests.get(url)
if get.status_code == requests.codes.ok:
    html = bs4.BeautifulSoup(get.text, features="html.parser")
    data = html.find(class_="grid-row list-content").find_all(class_="media")
    for item in data:
        articel = {}
        articel['image'] = item.find("img")["src"]
        articel['title'] = item.find(class_="media__title").get_text()
        articel['date'] = item.find(class_="media__date").find('span').get_text()
        articel['link'] = item.find("a")["href"]
        all_articel.append(articel)

print(all_articel)

