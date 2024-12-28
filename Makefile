migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

super-user:
	python manage.py createsuperuser

run-server:
	python manage.py runserver

install-depenencies:
	pip install -r requirements.txt
