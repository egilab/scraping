import csv
import requests

url = 'https://www.grafeauction.com/api/v1/events/829/lots?limit=0&page=1&search=&showClosed=false&myWatchedLots=false&myWonLots=false&myBids=false&order=sale_order&sort=asc'
get = requests.get(url).json()
try:
    data = get['lots']
    with open('test.csv', mode='w') as csv_file:
        fieldnames = ['slug', 'qty', 'asking_price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            output = {
                    "slug": item['slug'],
                    "qty": item['qty'],
                    "asking_price": item['asking_price']['amount']
            }
            writer.writerow(output)
except:
    print('error')
