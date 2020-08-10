import xlsxwriter
import requests

url = 'https://www.grafeauction.com/api/v1/events/829/lots?limit=0&page=1&search=&showClosed=false&myWatchedLots=false&myWonLots=false&myBids=false&order=sale_order&sort=asc'
get = requests.get(url).json()
try:
    data = get['lots']
    header = ['slug', 'qty', 'asking_price']
    dokumen = xlsxwriter.Workbook('fileku.xlsx')
    sheet = dokumen.add_worksheet()

    i = 0
    for item in data:
        output = {
            "slug": item['slug'],
            "qty": item['qty'],
            "asking_price": item['asking_price']['amount']
        }
        if i == 0:
            for col_num, data in enumerate(header):
                sheet.write(0, col_num, data)
        else:
            col_data = [item['slug'], item['qty'], item['asking_price']['amount']]
            for col_numx, datax in enumerate(col_data):
                sheet.write(i, col_numx, datax)
        i += 1
    dokumen.close()
except:
    print('error')
