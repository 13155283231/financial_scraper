django-admin startproject mysite		//���� django����


python manage.py runserver			//������վ


python manage.py startapp polls			//����һ��Ӧ�ó���

python manage.py migrate			//��ʼ�����ݿ� ������Ҫ�ı�


python manage.py makemigrations polls		//����Ǩ���ļ�


python manage.py sqlmigrate polls 0001		//��ӡ���� ���ݿⴴ�� �����ṩ���� ��������ȥ���ݿ�ִ��


python manage.py check				//������������ʲô����

python manage.py migrate			//������Զ��������ݿ�ı�

python manage.py shell				//�򿪽���ʽshell���������е���ʽ��������



python manage.py createsuperuser		//���������û�


ctrl+shift+g			//��ת����ǰ���� F12

alt+shift+f			//��������



python manage.py dumpdata comment_scraper > cdump.json

python manage.py dumpdata dynamic_scraper > ddump.json

//���ݿ�Ǩ�Ƶ�ʱ����

python manage.py loaddata cdump.json
