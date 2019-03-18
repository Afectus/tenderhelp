Для запуска веб сервера необходимо:<br>
1)Установить python библиотеки из файла requirements.txt<br>
2)Создать базу при текущих настройка необходима база postgres.<br>
Настройки подключения:<br>
  'NAME': 'tenderhelp',<br>
	'USER': 'tenderhelp',<br>
	'PASSWORD': 'tenderhelp',<br>
	'HOST': '127.0.0.1',<br>
  'PORT': '5432'<br>
 3)Из корня проекта выполнить команду python manage.py makemigrations<br>
 4)Из корня проекта выполнить команду python manage.py runserver<br>
