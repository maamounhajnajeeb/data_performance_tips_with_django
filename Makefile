.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: super-user
super-user:
	python manage.py createsuperuser

.PHONY: run-server
run-server:
	python manage.py runserver

.PHONY: install-depenencies
install-depenencies:
	pip install -r requirements.txt
