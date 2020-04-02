Twórcy Paweł Petelwicz, Kacper Kwitek, Agnieszka Talaga
Projekt polega na tym iż użytkownicy zamieszczają ogłoszenia, co chieliby wymienić, podczas przeglądania ogłoszeń można złożyć propozycję wymiany.

Uruchamianie projektu

git clone link do repozytorium
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
The project will be available at 127.0.0.1:8000.
