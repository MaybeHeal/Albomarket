from db import DataBase
import requests
import time


def item_names_data():
    response = requests.get('https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json').json()
    db = DataBase()
    for item in response:
        db.add_item(table='item_names', column='unique_name', value=item['UniqueName'])


def market_places_data():
    response = requests.get('https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/world.json').json()
    db = DataBase()
    for location in response:
        if (('Market' in location['UniqueName'] or 'Rest' in location['UniqueName']) and
                'Auction' not in location['Index']):
            db.add_items(table='markets', columns=('index', 'unique_name'),
                                 values=(location['Index'], location['UniqueName']))
        elif location['UniqueName'] == 'Caerleon':
            db.add_items(table='markets', columns=('index', 'unique_name'),
                                 values=(location['Index'], location['UniqueName']))


def market_categories_and_subcategories_data():
    response = requests.get('https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/items.json').json()
    db = DataBase()
    for category in response['items']['shopcategories']['shopcategory']:
        db.add_item(table='categories', column='category', value=category['@id'])


if __name__ == '__main__':
    start_time = time.time()
    item_names_data()
    market_places_data()
    market_categories_and_subcategories_data()
    end_time = time.time()
    print('Time:', end_time - start_time)
