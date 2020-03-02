Použité knihovny: django 3.0.3,
                  ares-util 0.2.0 (validace iča)
                  
Postup instalace: 

1) git clone https://github.com/Simecekk/proboston_task.git && cd proboston_task
2) pip install requirements.txt
3) python manage.py migrate
4) python manage.py runserver

endpoints: 
1) 127.0.0.1:8000 --> Stránka pro zadání formuláře
2) 127.0.0.1:8000/admin --> stránka administrace, je potřeba vytvořit superuser účet (python manage.py createsuperuser).
