CREATE TABLE IF NOT EXISTS 'item_names' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'unique_name' TEXT
);

CREATE TABLE IF NOT EXISTS 'markets' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'index' TEXT,
    'unique_name' TEXT
);

CREATE TABLE IF NOT EXISTS 'categories' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'category' TEXT
);

CREATE TABLE IF NOT EXISTS 'subcategories' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'subcategory' TEXT,
    'category' TEXT,
    FOREIGN KEY ('category') REFERENCES 'categories'('id')
);