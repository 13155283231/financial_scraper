# coding:utf-8
import sqlite3

def select_by_stock_code(str_code):
    cx = sqlite3.connect("db.sqlite3")
    cu=cx.cursor()         
    cu.execute('select title from comment_scraper_comment where stock_code=%d'% str_code )
    values = cu.fetchall()
    cu.close()
    cx.close()
    return values

# 返回 stock_code,title
def select_two(str_code):
    cx = sqlite3.connect("db.sqlite3")
    cu=cx.cursor()         
    cu.execute('select stock_code,stock_name from comment_scraper_comment where stock_code=%d'% str_code )
    values = cu.fetchone()
    cu.close()
    cx.close()
    return values

def insert_sentiment(l):
    cx = sqlite3.connect("db.sqlite3")
    cu=cx.cursor()         
    r=cu.execute("insert into comment_scraper_analysis\
               (stock_code, stock_name,pos_degree,key) \
               values (?, ?, ?, ?)", (l[0], l[1],l[2],1))
    cx.commit()
    cu.close()
    cx.close()
    return r
    
