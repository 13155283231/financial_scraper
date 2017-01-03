# encoding=utf-8
import sqlite3
f = open("comment_unprocessed.txt","w")
cx = sqlite3.connect("db.sqlite3")

cu=cx.cursor()         
cu.execute('select * from comment_scraper_comment')
values = cu.fetchall()
for each in values:
    aa=each[1].replace(u'\xa0', u' ')           # 加上这段ok！
    print (aa)
    f.write(each[1].encode('utf-8'))
cu.close()              
cx.close()              
f.close()              

print "\n"
raw_input('按键任意键结束'.decode("utf-8").encode("gbk"))
