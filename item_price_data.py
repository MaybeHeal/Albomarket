from db import DataBase
import requests
import gzip


def item_price(items, locations, qualities):
    response = requests.get(f'https://west.albion-online-data.com/api/v2/stats/Prices/'
                            f'{items}.JSON?locations={locations}&qualities={qualities}',
                            headers={'Accept-Encoding': 'gzip'})
    print(response.json())


if __name__ == '__main__':
    item_price()
