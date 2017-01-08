import sqlite3

def select_by_stock_code(str_code):
    cx = sqlite3.connect("db.sqlite3")
    cu=cx.cursor()         
    cu.execute('select title from comment_scraper_comment where stock_code=%d'% str_code )
    values = cu.fetchall()
    return values
