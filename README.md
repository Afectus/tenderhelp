Для запуска веб сервера необходимо:
1)Установить python библиотеки из файла requirements.txt
2)Создать базу при текущих настройка необходима база postgres. 
Настройки подключения:
  'NAME': 'tenderhelp',
	'USER': 'tenderhelp',
	'PASSWORD': 'tenderhelp',
	'HOST': '127.0.0.1',
  'PORT': '5432'
 3)Из корня проекта выполнить команду python manage.py makemigrations
 4)Из корня проекта выполнить команду python manage.py runserver
