import requests
import bs4

url = 'https://jadwalsholat.pkpu.or.id/?id=13'
get = requests.get(url)
if get.status_code == requests.codes.ok:
    soup = bs4.BeautifulSoup(get.text, features="html.parser")
    data = soup.find('tr', 'table_highlight')
    jadwal = {}
    i = 0
    for d in data:
        if i == 1:
            jadwal['zuhur'] = d.get_text()
        elif i == 2:
            jadwal['ashar'] = d.get_text()
        elif i == 3:
            jadwal['magrib'] = d.get_text()
        elif i == 4:
            jadwal['isya'] = d.get_text()
        elif i == 5:
            jadwal['subuh'] = d.get_text()

        i += 1
else:
    print('url not found')
print('\ntanggal berjalan')
print(jadwal)

print('\nSemua tanggal')
match = ['table_light', 'table_highlight', 'table_dark']
data_all = soup.find_all('tr')
jadwal_allsx = []
for x in data_all:
    if x['class'][0] in match:
        # by list
        # jadwal_alls = []
        # jadwal_alls.append(x.find_all('td')[0].get_text())
        # jadwal_alls.append(x.find_all('td')[1].get_text())
        # jadwal_alls.append(x.find_all('td')[2].get_text())
        # jadwal_alls.append(x.find_all('td')[3].get_text())
        # jadwal_alls.append(x.find_all('td')[4].get_text())
        # jadwal_alls.append(x.find_all('td')[5].get_text())
        # jadwal_allsx.append(jadwal_alls)

        # by dictionary
        jadwal_all = {}
        jadwal_all['tanggal'] = x.find_all('td')[0].get_text()
        jadwal_all['subuh'] = x.find_all('td')[1].get_text()
        jadwal_all['zuhur'] = x.find_all('td')[2].get_text()
        jadwal_all['ashar'] = x.find_all('td')[3].get_text()
        jadwal_all['magrib'] = x.find_all('td')[4].get_text()
        jadwal_all['isya'] = x.find_all('td')[5].get_text()
        jadwal_allsx.append(jadwal_all)

print(jadwal_allsx)
