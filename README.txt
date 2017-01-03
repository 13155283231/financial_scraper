django-admin startproject mysite		//创建 django工程


python manage.py runserver			//运行网站


python manage.py startapp polls			//创建一个应用程序

python manage.py migrate			//初始化数据库 建立必要的表


python manage.py makemigrations polls		//生成迁移文件


python manage.py sqlmigrate polls 0001		//打印命令 数据库创建 给人提供建议 但并不会去数据库执行


python manage.py check				//检查服务器出了什么问题

python manage.py migrate			//这才是自动创建数据库的表

python manage.py shell				//打开交互式shell，以命令行的形式插入数据



python manage.py createsuperuser		//创建超级用户


ctrl+shift+g			//跳转到当前方法 F12

alt+shift+f			//查找引用



python manage.py dumpdata comment_scraper > cdump.json

python manage.py dumpdata dynamic_scraper > ddump.json

//数据库迁移的时候用

python manage.py loaddata cdump.json
